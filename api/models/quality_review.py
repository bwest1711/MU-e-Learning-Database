from database import db
from sqlalchemy.orm import relationship, backref
from datetime import date

################################################################################
# Quality reviews are performed on course versions (NOT sections!) on a
# recurring basis. They are a back-and-forth process between the author of the
# course version and an instructional designer, so we track the different stages
# of the review using this object. 
################################################################################

class QualityReview(db.Model):
    __tablename__ = 'qualityReview'

    id = db.Column(db.Integer, primary_key=True)

    # Course Version that this review is assigned to
    courseVersion = db.Column(db.Integer, db.ForeignKey('courseVersion.id'))

    # Current stage that the review is in, numbered 0 to 5. 
    # 0 - Author performs quality assessment
    # 1 - Instructional designer performs quality assessment
    # 2 - Author & I.D. meet to discuss changes
    # 3 - Author implements changes
    # 4 - I.D. signs off on changes
    # 5 - Quality review is finished
    stage = db.Column(db.Integer)

    # Date that quality review began
    startDate = db.Column(db.Date)

    # Date that quality review was finished (when 'stage' changed to 5)
    endDate = db.Column(db.Date)

    # Back reference to all the notes assigned to this quality review
    notes = relationship('Note')

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
              'endDate': self.endDate.isoformat(),
              'notes': [n.id for n in notes]
              }
