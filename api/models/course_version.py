from database import db
from sqlalchemy.orm import relationship, backref

################################################################################
# Course Versions are a sort of semester-long 'lesson plan.' Instructors author
# them, and they are then taught (as Sections) during the school year. 
# According to Dr. Rubin, most courses have a 'master version' that instructors
# teach, but sometimes, instructors will teach their own version of a course. 
#
# We need to ensure that *all* versions of every course are compliant with
# divisional standards, so we track the quality and compliance of each version.
################################################################################

class CourseVersion(db.Model):
    __tablename__ = 'courseVersion'

    id = db.Column(db.Integer, primary_key=True)

    # Course that this is a version of
    course = db.Column(db.Integer, db.ForeignKey('course.id'))

    # Instructor that authored this version
    instructor = db.Column(db.Integer, db.ForeignKey('instructor.id'))

    # A short label that the author assigns to the course. Might be something
    # like "PHY121 Master Version", or "Enhanced multimedia version"
    label = db.Column(db.String(64))

    # What format the course is in.
    # 0 - Online Only
    # 1 - Hybrid / Partially Online
    # 2 - IVDL (Interactive Video Distance Learning)
    # 3 - Face-to-Face Enhanced
    # TODO Change to an integer enum instead of string-typing!
    courseType = db.Column(db.String(64))

    # Whether the materials used in the version are copyright compliant
    copyrightCompliant = db.Column(db.Boolean)

    # Whether the version is compliant with ADA
    adaCompliant = db.Column(db.Boolean)
    # The year of ADA compliance (standards change between e.g. 2006 and 2009)
    adaYear = db.Column(db.Integer)

    # Back references to sections using this version, and quality reviews
    # that have been done on this version
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
