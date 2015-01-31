from database import db
from sqlalchemy.orm import relationship, backref

class Instructor(db.Model):
    __tablename__ = 'instructor'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    email = db.Column(db.String(64))

    course_versions = relationship('CourseVersion', backref='instructor')

    def __init__(self, full_name, email=''):
        self.full_name = full_name
        self.email = email

    def __repr__(self):
        return '<{0}>'.format(self.full_name)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'course_versions': [cv.id for cv in self.course_versions]
            }
