from database import db
from sqlalchemy.orm import relationship, backref

class CourseVersion(db.Model):
    __tablename__ = 'course_version'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    label = db.Column(db.String(64))

    def __init__(self, course_id, instructor_id, label):
        self.course_id = course_id
        self.instructor_id = instructor_id
        self.label = label

    def __repr__(self):
        return '<course:{0} instr:{1} "{2}">'.format(self.course_id, 
                                                     self.instructor_id, 
                                                     self.label)

    @property
    def to_json(self):
          return {
              'id': self.id,
              'course_id': self.course_id,
              'instructor_id': self.instructor_id,
              'label': self.label
              }
