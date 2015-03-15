from database import db
from sqlalchemy.orm import relationship, backref

################################################################################
# We need to have a department object in order to display information about
# administrators, and track the different names that are assigned to certain 
# departments (like how Zoology and Botany got merged into Biology). 
################################################################################

class Department(db.Model):
    __tablename__ = 'department'
    
    id = db.Column(db.Integer, primary_key=True)

    # Full name, like "Political Science"
    name = db.Column(db.String(255))

    # Short name, like "POL" or "BIO"
    abbreviation = db.Column(db.String(255))

    # Short division name, like "CAS" or "CEC"
    division = db.Column(db.String(255))

    # Full name of dept. chair / provost / administrator / whoever's in charge
    admin = db.Column(db.String(255))

    # Email of said administrator
    adminEmail = db.Column(db.String(255))

    # 'aliases' is a semicolon-separated list of previous names for this
    # department, e.g. for Biology, "ZOO-Zoology;MBI-Microbiology"

    # Really, this 'should' be its own table, but since aliases won't be all
    # that common (maybe ~1 alias for every 10 departments), it's less complex 
    # to just store it this way. 
    aliases = db.Column(db.String(1024))

    # Back reference to all courses that are assigned to this department
    courses = relationship('Course')

    def __init__(self, name, abbreviation, admin, adminEmail, aliases=""):
        self.name = name
        self.abbreviation = abbreviation
        self.admin = admin
        self.adminEmail = adminEmail
        self.aliases = aliases

    @property
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'abbreviation': self.abbreviation,
            'admin': self.admin,
            'adminEmail': self.adminEmail,
            'aliases': self.aliases,
            'courses': [c.id for c in self.courses]
        }
