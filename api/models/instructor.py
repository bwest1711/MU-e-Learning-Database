from database import db

class Instructor(db.Model):
    __tablename__ = 'instructor'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    email = db.Column(db.String(64))

    def __init__(self, full_name, email=''):
        self.full_name = full_name
        self.email = email

    def __repr__(self):
        return '<{0}>'.format(self.full_name)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email
            }
