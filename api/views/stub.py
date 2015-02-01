from flask.ext import restful
from flask.ext.restful import reqparse
from database import db

# Collection of resources
class StubsAPI(restful.Resource):
    # Get the collection
    def get(self):
        # Get every object from the DB
        # Send back the list of objects
        return {'stub': 'stub'}

    # Add an item to the collection
    def post(self):
        # Create a new object from given args
        # Add object to the DB
        return {'stub': 'stub'}

# Individual resource
class StubAPI(restful.Resource):
    # Get an item from the collection
    def get(self, id):
        # Get an object from the DB
        # Send back the retrieved object
        return {'stub': 'stub'}

    # Update an item in the collection
    def put(self, id):
        # Get an object from the DB
        # Update the boject with given args
        # Add object to the DB
        # Send back the created object
        return {'stub': 'stub'}

    def delete(self, id):
        # Get an object from the DB
        # Delete the object from the DB
        # Return success
        return {'stub': 'stub'}
