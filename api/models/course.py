from database import db
from sqlalchemy.orm import relationship, backref

class Course(db.Model):
    __tablename__ = 'course'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    department = db.Column(db.String(32))
    number = db.Column(db.Integer())

    courseVersions = relationship('CourseVersion')

    def __init__(self, title, department='NONE', number=0):
        self.title = title
        self.department = department
        self.number = number

    @property
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'department': self.department,
            'number': self.number,
            'courseVersions': [cv.id for cv in self.courseVersions]
        }
