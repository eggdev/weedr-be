from flask import Blueprint, Response, request
from database.models import User

users = Blueprint("users", __name__)


@users.route("/users")
# Fetch all users from db
def get_all_users():
    users = User.objects().to_json()
    return {"users": users}, 200


@users.route("/users/<string:name>")
# Get single user
def get_one_user(name):
    found = User.objects.get(name=name).to_json()
    return found, 200


@users.route('/users', methods=['POST'])
# Add new user
def add_user():
    body = request.get_json()
    new_user = User(**body).save()
    name = new_user.name
    return {"id": name}, 200


@users.route('/users/<string:name>', methods=["PUT"])
# Users can get updated
def update_user(name):
    body = request.get_json()
    User.objects.get(name=name).update(**body)
    updated_user = User.objects.get(name=body["name"]).to_json()
    return updated_user, 200


@users.route('/users/<string:name>', methods=["DELETE"])
# Users can be deleted
def delete_user(name):
    deleted = User.objects().get(name=name)
    deleted.delete()
    return deleted.to_json(), 200
