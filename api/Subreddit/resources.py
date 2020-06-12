#  Store subreddits that users have logged in from.
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class GetSubreddit(Resource):
    @jwt_required
    def get(self, sr):
        curr_user = get_jwt_identity()
        resp = make_response({"subreddit": sr}, 200)
        return resp
