#!/usr/bin/python

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class Production(Config):
    pass
    
class Development(Config):
    DEBUG = True
