#  Capture all reported items for this subreddit
from flask import Response, request, jsonify
from flask_restful import Resource
# from database.models import Reported_Item

# When subreddit is generated, pull in info from it to define the schema around what mods exist
# Should be able to get that information and apply it to the collection


class GetAllReportedItems(Resource):
    def get(self, subreddit):
        print(subreddit)
        items = ["value"]
        # This will need to be all subreddit data we want to pass to FE
        return Response(items, mimetype="application/json", status=200)

    def post(self, subreddit):
        body = request.get_json()
        # new_user = Reported_Users(**body).save()
        # Probably only used on sub creation? Maybe on new reported_user?
        return Response(body, mimetype="application/json", status=200)
