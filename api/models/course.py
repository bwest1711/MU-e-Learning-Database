from database import db
from sqlalchemy.orm import relationship, backref

################################################################################
# Courses are, in this domain, a collection of course versions that all teach
# the same concepts. They're not directly taught (those are course sections) and
# not directly authored (those are course versions). They can be crosslisted
# between multiple departments.
################################################################################

class Course(db.Model):
    __tablename__ = 'course'
    
    id = db.Column(db.Integer, primary_key=True)

    # e.g. 121 "Introduction to Financial Accounting"
    number = db.Column(db.Integer())
    title = db.Column(db.String(255))

    # The main (?) department that this course belongs to
    # TODO Crosslisting
    department = db.Column(db.Integer, db.ForeignKey('department.id'))

    # Back reference to course versions assigned to this course
    courseVersions = relationship('CourseVersion')

    def __init__(self, title, department=0, number=0):
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
