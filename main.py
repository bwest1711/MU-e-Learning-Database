#!/usr/bin/python
'''Flask app'''

from database import db
from flask import Flask

from client.views import client_app
from todo.views import root_app
from api.rest import api_app


def create_app():
    '''Initialize Flask and SQLAlchemy contexts and register blueprints'''
    app = Flask(__name__)
    db.init_app(app)

    app.register_blueprint(client_app)
    app.register_blueprint(root_app)
    app.register_blueprint(api_app)
    return app
