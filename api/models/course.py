from database import db
from sqlalchemy.orm import relationship, backref

class Course(db.Model):
    __tablename__ = 'course'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    department = db.Column(db.String(32))
    number = db.Column(db.Integer())

    course_versions = relationship('CourseVersion', backref='course')

    def __init__(self, title, department='NONE', number=0):
        self.title = title
        self.department = department
        self.number = number

    def __repr__(self):
        return '<{0}{1} "{2}">'.format(self.department, self.number, self.title)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'department': self.department,
            'number': self.number,
            'course_versions': [cv.id for cv in self.course_versions]
        }
