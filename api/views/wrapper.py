from flask.ext import restful
from flask.ext.restful import reqparse
from database import db

class PluralWrapperAPI(restful.Resource):
    '''Provides a simple wrapper around a collection of items in a SQLAlchemy
    database model.'''

    def get(self):
        '''Get the collection of items'''
        items = self._model_class.query.order_by(self._model_class.id.asc()).all()
        items_json = [i.to_json for i in items]
        return { self._plural_name: items_json }

    def post(self):
        '''Add a new item to the collection'''
        # Parse request arguments
        parser = reqparse.RequestParser()
        for arg, arg_type in self._reqd_args.items():
            parser.add_argument(arg, type=arg_type, required=True)
        for arg, arg_type in self._opt_args.items():
            parser.add_argument(arg, type=arg_type, required=False)
        args = parser.parse_args()

        # Fail if there are any arguments in _reqd_args that *aren't* in the 
        # parsed arguments
        missing_reqd_args = [reqd_arg for reqd_arg, arg_type 
                             in self._reqd_args.items()
                             if reqd_arg not in args]
        missing_reqd_args_msg = "Missing one or more required fields: {}"
        if len(missing_reqd_args) > 0:
            restful.abort(400, message=missing_reqd_args_msg.format(missing_reqd_args))

        item = self._model_class(**args)
        db.session.add(item)
        db.session.commit()
        return { self._singular_name: item.to_json }


class SingularWrapperAPI(restful.Resource):
    '''Provides a simple wrapper around a single item in a collection of
    SQLAlchemy database objects.'''

    def get(self, id):
        '''Get a single item from the collection'''
        item = self._model_class.query.get(id)
        if not item:
            restful.abort(404, message="Invalid {}".format(self._singular_name))
        return { self._singular_name: item.to_json }

    def put(self, id):
        '''Modify an item in the collection'''
        # Get the requested item
        item = self._model_class.query.get(id)
        if not item:
            restful.abort(404, message="Invalid {}".format(self._singular_name))

        # Parse request arguments
        # In PUT, no arguments are required, and attributes retain their
        # previous values - unlike similar code in POST
        parser = reqparse.RequestParser()
        for arg, arg_type in self._reqd_args.items():
            parser.add_argument(arg, type=arg_type, default=getattr(item, arg))
        for arg, arg_type in self._opt_args.items():
            parser.add_argument(arg, type=arg_type, default=getattr(item, arg))
        args = parser.parse_args()

        # Set the requested attributes to their new values
        for arg, value in args.items():
            setattr(item, arg, value)

        db.session.add(item)
        db.session.commit()
        return { self._singular_name: item.to_json }

    def delete(self, id):
        '''Delete an item from the collection'''
        item = self._model_class.query.get(id)
        if not item:
            restful.abort(404, message="Invalid {}".format(self._singular_name))
        db.session.delete(item)
        db.session.commit()


def make_wrapper_api(model_class, singular_name, plural_name, reqd_args, opt_args):
    '''Constructs two simple CRUD API wrappers around a given base class. 
    Individual items will be accessible at '/{singular_name}/{id}'; the whole
    collection will be accessible at '/{plural_name}'.'''
    def __init__(self):
        self._model_class = model_class
        self._singular_name = singular_name
        self._plural_name = plural_name
        self._reqd_args = reqd_args
        self._opt_args = opt_args
    singular_api = type(model_class.__name__ + 'API', (SingularWrapperAPI,), 
                {"__init__": __init__})
    plural_api =  type(model_class.__name__ + 'sAPI', (PluralWrapperAPI,), 
                {"__init__": __init__})
    apis = (singular_api, plural_api)
    return apis
