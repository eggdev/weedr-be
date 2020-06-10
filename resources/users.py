from flask import Response, request
from database.models import User
from flask_restful import Resource


class UsersApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        new_user = User(**body).save()
        return Response(new_user, mimetype="application/json", status=200)


class UserApi(Resource):
    def get_one(self, name):
        found = User.objects.get(name=name).to_json()
        return Response(found, mimetype="application/json", status=200)

    def update_one(self, name):
        body = request.get_json()
        updated = User.objects.get(name=name).update(**body).to_json()
        return Response(updated, mimetype="application/json", status=200)

    def delete_one(self, name):
        deleted = User.objects().get(name=name)
        deleted.delete()
        return Response(deleted, mimetype="application/json", status=200)
