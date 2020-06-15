import datetime
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                set_access_cookies,
                                set_refresh_cookies,
                                unset_jwt_cookies,
                                get_jwt_identity)
from database.User.models import User
from database.Subreddit.models import Subreddit


class SubredditRequests(Resource):
    @jwt_required
    def get(self, subreddit):
        curr = get_jwt_identity()
        reddit = User.objects.get(username=curr).generate_praw_instance()
        try:
            sr = Subreddit.objects.get(sr=subreddit)
            sub = reddit.subreddit(sr.sr)
            return_obj = sr.make_return_object(sub)
            resp = make_response(return_obj, 200)
            return resp
        except Subreddit.DoesNotExist:
            resp = make_response(
                {"error": "No subreddit info found. No mods have signed up"}, 200)
            return resp
