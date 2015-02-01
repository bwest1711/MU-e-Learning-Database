from database import db
from sqlalchemy.orm import relationship, backref

class CourseSection(db.Model):
    __tablename__ = 'course_section'

    id = db.Column(db.Integer, primary_key=True)
    course_version_id = db.Column(db.Integer, db.ForeignKey('course_version.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    semester = db.Column(db.String(16))

    def __init__(self, course_version_id, instructor_id, semester):
        self.course_version_id = course_version_id
        self.instructor_id = instructor_id
        self.semester = semester

    def __repr__(self):
        return '<course:{0} instr:{1} "{2}">'.format(self.course_version_id, 
                                                     self.instructor_id, 
                                                     self.semester)

    @property
    def to_json(self):
          return {
              'id': self.id,
              'course_version_id': self.course_version_id,
              'instructor_id': self.instructor_id,
              'semester': self.semester
              }
