from database import db
from sqlalchemy.orm import relationship, backref

class QualityReview(db.Model):
    __tablename__ = 'qualityReview'

    id = db.Column(db.Integer, primary_key=True)
    courseVersion = db.Column(db.Integer, db.ForeignKey('courseVersion.id'))
    stage = db.Column(db.String(16))

    def __init__(self, courseVersion, stage):
        self.courseVersion = courseVersion
        self.stage = stage

    @property
    def to_json(self):
          return {
              'id': self.id,
              'courseVersion': self.courseVersion,
              'stage': self.stage
              }
