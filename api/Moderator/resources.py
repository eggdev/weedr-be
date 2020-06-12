#  Capture all reported items for this subreddit
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
from database.Moderator.models import Moderator
from database.Subreddit.models import Subreddit
from reddit.config import reddit


class CreateModerator(Resource):
    def post(self):
        body = request.get_json()
        username = body["username"].lower()
        try:
            Moderator.objects.get(username=username)
            resp = make_response({"found": "User already exists"}, 201)
            return resp
        except Moderator.DoesNotExist:
            is_mod = reddit.redditor(name=username).is_mod
            if is_mod:
                new_mod = Moderator(username=username)
                new_mod.generate_moderated_subreddits(reddit)
                new_mod.password = body["password"]
                new_mod.hash_password()
                # Generate new user object with password
                new_mod.save()
                return_obj = new_mod.generate_return_object()
                resp = make_response(return_obj, 200)
                return resp
            else:
                # Some day, looking for moderator dashboard? Job listing sort of thing?
                resp = make_response({"error": "User is not a moderator"}, 501)
                return resp


class LoginModerator(Resource):
    def post(self):
        body = request.get_json()
        username = body.get('username').lower()
        try:
            moderator = Moderator.objects.get(username=username)
            # Checking if users password is correct
            authorized = moderator.check_password(body.get('password'))
            if not authorized:
                return {'error': 'Email or password invalid', "login": False}, 401
            access_token = create_access_token(
                identity=str(moderator.username)
            )
            refresh_token = create_refresh_token(
                identity=str(moderator.username)
            )

            return_obj = moderator.generate_return_object()
            resp = make_response(return_obj, 200)
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp
        except Moderator.DoesNotExist:
            resp = make_response(
                {"error": "User was not found.", "msg": "Would you like to create a new one?"}, 401)
            return resp


class LogoutModerator(Resource):
    def post(self):
        resp = make_response({"login": False}, 200)
        unset_jwt_cookies(resp)
        return resp


class GetModerator(Resource):
    @jwt_required
    def get(self):
        curr = get_jwt_identity()
        mod_user = Moderator.objects.get(username=curr)
        return_obj = mod_user.generate_return_object()
        resp = make_response({"user": return_obj}, 200)
        # Create new praw reddit instance
        return resp
