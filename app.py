from flask import Flask, request
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from database.db import initialize_app
from database.models import User
from reddit.config import subreddit
from reddit.app import collect_recently_reported_users

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'host': f'mongodb://localhost/{subreddit}'
}

initialize_app(app)


@ app.route("/users")
# Fetch all users from db
def get_all_users():
    users = User.objects().to_json()
    return {"users": users}, 200


@ app.route("/users/<string:name>")
# Get single user
def get_one_user(name):
    found = User.objects.get(name=name).to_json()
    return found, 200


@ app.route('/users', methods=['POST'])
# Add new user
def add_user():
    body = request.get_json()
    new_user = User(**body).save()
    name = new_user.name
    return {"id": name}, 200


@ app.route('/users/<string:name>', methods=["PUT"])
# Users can get updated
def update_user(name):
    body = request.get_json()
    User.objects.get(name=name).update(**body)
    updated_user = User.objects.get(name=body["name"]).to_json()
    return updated_user, 200


@ app.route('/users/<string:name>', methods=["DELETE"])
# Users can be deleted
def delete_user(name):
    deleted = User.objects().get(name=name)
    deleted.delete()
    return deleted.to_json(), 200


if __name__ == "__main__":
    app.run()
