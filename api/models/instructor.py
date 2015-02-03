from database import db
from sqlalchemy.orm import relationship, backref

class Instructor(db.Model):
    __tablename__ = 'instructor'

    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(255))
    email = db.Column(db.String(64))

    courseVersions = relationship('CourseVersion')
    courseSections = relationship('CourseSection')

    def __init__(self, fullName, email=''):
        self.fullName = fullName
        self.email = email

    @property
    def to_json(self):
        return {
            'id': self.id,
            'fullName': self.fullName,
            'email': self.email,
            'courseVersions': [cv.id for cv in self.courseVersions],
            'courseSections': [cs.id for cs in self.courseSections]
            }
