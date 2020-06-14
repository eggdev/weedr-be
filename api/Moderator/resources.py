import datetime
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from reddit.config import reddit, scope_list
from database.User.models import User


class ModAuth(Resource):
    @jwt_required
    def get(self):
        auth_url = reddit.auth.url(scope_list, 'state_val', 'permanent')
        return auth_url, 200
