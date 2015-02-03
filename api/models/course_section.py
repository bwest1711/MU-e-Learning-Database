from database import db
from sqlalchemy.orm import relationship, backref

class CourseSection(db.Model):
    __tablename__ = 'courseSection'

    id = db.Column(db.Integer, primary_key=True)
    courseVersion = db.Column(db.Integer, db.ForeignKey('courseVersion.id'))
    instructor = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    semester = db.Column(db.String(16))

    def __init__(self, courseVersion, instructor, semester):
        self.courseVersion = courseVersion
        self.instructor = instructor
        self.semester = semester

    @property
    def to_json(self):
          return {
              'id': self.id,
              'courseVersion': self.courseVersion,
              'instructor': self.instructor,
              'semester': self.semester
              }
