from database import db

class Todo(db.Model):
  ''' Todo representation '''
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(512))

  is_completed = db.Column(db.Boolean, default=False)

  added_on = db.Column(db.DateTime,
    default=db.func.now())

  last_update = db.Column(db.DateTime,
      default=db.func.now(),
      onupdate=db.func.now())

  def __init__(self, description):
    self.description = description

  def __repr__(self):
    return '<{0}>'.format(self.description)

  def as_json(self):
    return {'id': self.id,
        'description': self.description,
        'isCompleted': self.is_completed,
        'lastUpdate': self.last_update.strftime('%s')}


class Instructor(db.Model):
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


class Course(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255))
  department = db.Column(db.String(32))
  number = db.Column(db.Integer())

  def __init__(self, title, department='NONE', number=0):
      self.title = title
      self.department = department
      self.number = number

  def __repr__(self):
    return '<{0}{1} "{2}">'.format(self.department, self.number, self.title)

  @property
  def to_json(self):
    return {
        'id': self.id,
        'title': self.title,
        'department': self.department,
        'number': self.number
        }
