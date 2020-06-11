from flask import Response, request, jsonify
from database.models import Reported_Users
from flask_restful import Resource
from reddit.config import reddit
from resources.formatting import format_user_object


class ManyUsersApi(Resource):
    def get(self):
        users = Reported_Users.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        new_user = Reported_Users(**body).save()
        return Response(new_user, mimetype="application/json", status=200)


class SingleUserApi(Resource):
    def get(self, name):
        found = Reported_Users.objects.get(name=name)
        formatted = format_user_object(found)
        return Response(formatted, mimetype="application/json", status=200)

    def put(self, name):
        body = request.get_json()
        updated = Reported_Users.objects.get(
            name=name).update(**body).to_json()
        return Response(updated, mimetype="application/json", status=200)

    def delete(self, name):
        deleted = Reported_Users.objects().get(name=name)
        deleted.delete()
        return Response(deleted, mimetype="application/json", status=200)
