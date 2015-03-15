from database import db
from sqlalchemy.orm import relationship, backref

################################################################################
# Instructors can author course versions, and teach course sections. An
# authenticated user can only modify a version or section if the 'instructor'
# field matches their UniqueID.
################################################################################

class Instructor(db.Model):
    __tablename__ = 'instructor'

    id = db.Column(db.Integer, primary_key=True)

    # Full name of the instructor. Note that to avoid the confusion caused by
    # multicultural naming schemes, we don't distinguish first name, last name,
    # title, etc.
    fullName = db.Column(db.String(255))

    # Email that we'll be using to contact the instructor.
    # Note that we can't just generate this from the UniqueID, because some
    # instructors have non-miamioh.edu addresses.
    email = db.Column(db.String(64))

    # Miami UniqueID of the instructor (e.g. 'kiperjd').
    # TODO Probably use this to ensure that instructors can only change their
    # own courses. Be aware of security implications
    uniqueid = db.Column(db.String(32))

    # Back reference to authored versions and taught sections
    courseVersions = relationship('CourseVersion')
    courseSections = relationship('CourseSection')

    def __init__(self, fullName, email='', uniqueid=''):
        self.fullName = fullName
        self.email = email
        self.uniqueid = uniqueid

    @property
    def to_json(self):
        return {
            'id': self.id,
            'fullName': self.fullName,
            'email': self.email,
            'uniqueid': self.uniqueid,
            'courseVersions': [cv.id for cv in self.courseVersions],
            'courseSections': [cs.id for cs in self.courseSections]
            }
