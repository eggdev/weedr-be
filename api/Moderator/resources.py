#  Capture all reported items for this subreddit
from flask import Response, request, jsonify
from flask_restful import Resource
from database.Moderator.models import Moderator
from reddit.config import reddit


class CreateModerator(Resource):
    def generate_user_object(self, username):
        new_moderator = {
            "username": username,
            "subreddits": []
        }
        moderated_subreddits = reddit.get(
            f"/user/{username}/moderated_subreddits")
        if "data" in moderated_subreddits:
            for sub in moderated_subreddits["data"]:
                # this method will grab all subreddit data
                new_moderator["subreddits"].append(sub["sr"])

        return new_moderator

    def post(self):
        body = request.get_json()
        username = body["username"].lower()
        try:
            found = Moderator.objects.get(username=username)
            # Log user in
            return {"found": "User already exists"}, 201
        except Moderator.DoesNotExist:
            is_mod = reddit.redditor(name=username).is_mod
            if is_mod:
                new_user_dict = self.generate_user_object(username)
                new_user_dict["password"] = body["password"]
                new_user = Moderator(**new_user_dict)
                new_user.hash_password()
                new_user.save()
                return {"username": new_user["username"]}, 200
            else:
                return {"rejected": "User is not a moderator"}, 501


class GetModerator(Resource):
    def get(self, username):
        # Create new praw reddit instance
        # Render available subreddits that they moderate
        return username
