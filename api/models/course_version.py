from database import db
from sqlalchemy.orm import relationship, backref

class CourseVersion(db.Model):
    __tablename__ = 'courseVersion'

    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Integer, db.ForeignKey('course.id'))
    instructor = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    label = db.Column(db.String(64))

    courseSections = relationship('CourseSection')

    def __init__(self, course, instructor, label):
        self.course = course
        self.instructor = instructor
        self.label = label

    @property
    def to_json(self):
        return {
            'id': self.id,
            'course': self.course,
            'instructor': self.instructor,
            'label': self.label,
            'courseSections': [cs.id for cs in self.courseSections]
            }
