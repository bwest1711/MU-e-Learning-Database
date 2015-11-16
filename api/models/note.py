from database import db
from sqlalchemy.orm import relationship, backref

################################################################################
# "Notes" are attachments and messages that are associated with a stage in the 
# quality review process. These can be brief notes like 'Instructional designer
# suggested more group work', or more detailed, like a PDF with meeting minutes.
################################################################################

class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)

    # Associated quality review
    qualityReview = db.Column(db.Integer, db.ForeignKey('qualityReview.id'))

    # Stage in the quality review process
    stage = db.Column(db.Integer)

    # Notes entered into the stage's text field
    text = db.Column(db.String(8192))

    # UUID of the associated document
    # TODO Figure out document storage scheme. Probably something like: 
    # mueldb.example.edu/docs/2u3inw34ghvrsnwjk3298cn34
    # Which returns a .pdf file
    attachment = db.Column(db.String(1024))

    #
    signature = db.Column(db.String(100))

    def __init__(self, qualityReview, signature, stage=0, text="", attachment=""):
        self.qualityReview = qualityReview
        self.stage = stage
        self.text = text
        self.attachment = attachment
        self.signature = signature

    @property
    def to_json(self):
        return {
            'id': self.id,
            'qualityReview': self.qualityReview,
            'stage': self.stage,
            'text': self.text,
            'attachment': self.attachment,
            'signature' : self.signature
        }
