from flask.ext import restful
from flask.ext.restful import reqparse
from database import db
from api.models.quality_review import QualityReview


class QualityReviewsAPI(restful.Resource):
    def get(self):
        '''Get list of all course sections'''
        quality_reviews = QualityReview.query.order_by(QualityReview.id.asc()).all()
        quality_reviews = [qr.to_json for qr in quality_reviews]
        return {'quality_reviews': quality_reviews}

    # TODO
    def post(self):
        pass


class QualityReviewAPI(restful.Resource):
    def get(self, id):
        '''Get a specific quality review'''
        quality_review = QualityReview.query.get(id)

        if not quality_review:
            restful.abort(404, message='Invalid quality review')

        return {'quality_review': quality_review.to_json}

    # TODO
    def put(self, id):
        pass

    # TODO
    def delete(self, id):
        pass
