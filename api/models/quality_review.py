from database import db
from sqlalchemy.orm import relationship, backref
from datetime import date

class QualityReview(db.Model):
    __tablename__ = 'qualityReview'

    id = db.Column(db.Integer, primary_key=True)
    courseVersion = db.Column(db.Integer, db.ForeignKey('courseVersion.id'))
    stage = db.Column(db.String(16))
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)

    def __init__(self, courseVersion, stage, 
                 startDate=date.today(), endDate=date.today()):
        self.courseVersion = courseVersion
        self.stage = stage
        self.startDate = startDate
        self.endDate = endDate

    @property
    def to_json(self):
          return {
              'id': self.id,
              'courseVersion': self.courseVersion,
              'stage': self.stage,
              'startDate': self.startDate.isoformat(),
              'endDate': self.endDate.isoformat()
              }
