#  Capture all reported items for this subreddit
import datetime
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from database.Moderator.models import Moderator
from reddit.config import reddit


class CreateModerator(Resource):
    def generate_mod_object(self, username):
        new_moderator = {
            "username": username,
            "subreddits": []
        }
        # Will check for all subreddits a user moderates and add them to the object
        moderated_subreddits = reddit.get(
            f"/user/{username}/moderated_subreddits")
        if "data" in moderated_subreddits:
            for sub in moderated_subreddits["data"]:
                new_moderator["subreddits"].append(sub["sr"])

        return new_moderator

    def post(self):
        body = request.get_json()
        username = body["username"].lower()
        try:
            Moderator.objects.get(username=username)
            return {"found": "User already exists"}, 201
        except Moderator.DoesNotExist:
            is_mod = reddit.redditor(name=username).is_mod
            if is_mod:
                # Create new moderator object without a password
                new_mod_dict = self.generate_mod_object(username)
                new_mod = Moderator(**new_mod_dict)
                new_mod["password"] = body["password"].hash_password()
                # Generate new user object with password
                new_mod.save()
                return {"success": {"username": username}}, 200
            else:
                return {"error": "User is not a moderator"}, 501


class LoginModerator(Resource):
    def post(self):
        body = request.get_json()
        username = body.get('username').lower()
        moderator = Moderator.objects.get(username=username)
        authorized = moderator.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid', "login": False}, 401

        access_token = create_access_token(
            identity=str(moderator.username))

        return {"login": True}, 200


class GetModerator(Resource):
    @jwt_required
    def get(self, username):
        moderator = Moderator.objects.get(username=username)
        # Change this to be oAuth at some point
        # Create new praw reddit instance
        # Generate a json for the FE of Moderator
        # JSON will contain each subreddit the user moderates and some basic json from that object

        return {"username": moderator.username}
