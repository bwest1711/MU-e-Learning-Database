from database import db
from sqlalchemy.orm import relationship, backref

################################################################################
# Sections are 'instances' of a Course, using a Course Version as a template. 
# By default, they should inherit the properties of the version they're using,
# but if the instructor makes any changes to the given materials, they need to
# affirm that their section of the course is, e.g., copyright and ADA compliant. 
################################################################################

class CourseSection(db.Model):
    __tablename__ = 'courseSection'

    id = db.Column(db.Integer, primary_key=True)

    # Version of the course that this section is using as a template
    courseVersion = db.Column(db.Integer, db.ForeignKey('courseVersion.id'))

    # Instructor that's actually teaching the section
    instructor = db.Column(db.Integer, db.ForeignKey('instructor.id'))

    # Semester that the section occurs in, stored as season followed by year
    # F - Fall, W - Winter, S - Spring, U - Summer
    # e.g. 'F13', 'W15', 'U14'
    semester = db.Column(db.String(16))

    # CRN of the course section
    crn = db.Column(db.String(16))

    # Whether or not the instructor has affirmed that this section is compliant
    # with all necessary standards 
    attested = db.Column(db.Boolean)

    # Date that the course must be attested by
    attestedDueDate = db.Column(db.Date)

    # Date that the instructor attested to the section's compliance
    attestedDate = db.Column(db.Date)

    # Name of the instructure that attested to the section's compliance
    attestedSignee = db.Column(db.String(255))


    def __init__(self, courseVersion, instructor, semester, crn,
                 attested=False, attestedDate=None, 
                 attestedDueDate=None, attestedSignee=''):
        self.courseVersion = courseVersion
        self.instructor = instructor
        self.semester = semester
        self.crn = crn
        self.attested = attested
        self.attestedDate = attestedDate
        self.attestedDueDate = attestedDueDate
        self.attestedSignee = attestedSignee

    @property
    def to_json(self):
          return {
              'id': self.id,
              'courseVersion': self.courseVersion,
              'instructor': self.instructor,
              'semester': self.semester,
              'attested': self.attested,
              'attestedDate': self.attestedDate
              }
