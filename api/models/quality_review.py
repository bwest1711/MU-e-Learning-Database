from database import db
from sqlalchemy.orm import relationship, backref

class QualityReview(db.Model):
    __tablename__ = 'quality_review'

    id = db.Column(db.Integer, primary_key=True)
    course_version_id = db.Column(db.Integer, db.ForeignKey('course_version.id'))
    stage = db.Column(db.String(16))

    def __init__(self, course_version_id, stage):
        self.course_version_id = course_version_id
        self.stage = stage

    def __repr__(self):
        return '<course:{0} {2}>'.format(self.course_version_id, 
                                         self.stage)

    @property
    def to_json(self):
          return {
              'id': self.id,
              'course_version_id': self.course_version_id,
              'stage': self.stage
              }
