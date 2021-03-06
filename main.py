#!/usr/bin/python
'''Flask app'''

from database import db
from flask import Flask

from client.views import client_app
from api.routes import create_api

def create_app():
    '''Initialize Flask and SQLAlchemy contexts and register blueprints'''
    app = Flask(__name__)
    db.init_app(app)

    app.register_blueprint(client_app)

    create_api(app, db)
    return app
