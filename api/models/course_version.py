from database import db
from sqlalchemy.orm import relationship, backref

class CourseVersion(db.Model):
    __tablename__ = 'courseVersion'

    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Integer, db.ForeignKey('course.id'))
    instructor = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    label = db.Column(db.String(64))
    courseType = db.Column(db.String(64))
    copyrightCompliant = db.Column(db.Boolean)
    adaCompliant = db.Column(db.Boolean)
    adaYear = db.Column(db.Integer)

    courseSections = relationship('CourseSection')
    qualityReviews = relationship('QualityReview')

    def __init__(self, course, instructor, label, courseType='Online Only',
                 copyrightCompliant=False, adaCompliant=False, adaYear=None):
        self.course = course
        self.instructor = instructor
        self.label = label
        self.courseType = courseType
        self.copyrightCompliant = copyrightCompliant
        self.adaCompliant = adaCompliant
        self.adaYear = adaYear

    @property
    def to_json(self):
        return {
            'id': self.id,
            'course': self.course,
            'instructor': self.instructor,
            'label': self.label,
            'courseType': self.courseType,
            'copyrightCompliant': self.copyrightCompliant,
            'adaCompliant': self.adaCompliant,
            'adaYear': self.adaYear,
            'courseSections': [cs.id for cs in self.courseSections],
            'qualityReviews': [qr.id for qr in self.qualityReviews]
            }
