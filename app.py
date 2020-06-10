from flask import Flask, request
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from database.db import initialize_app
from reddit.config import subreddit
from reddit.app import collect_recently_reported_users
from resources.users import users

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'host': f'mongodb://localhost/{subreddit}'
}
collect_recently_reported_users()
initialize_app(app)
app.register_blueprint(users)

if __name__ == "__main__":
    app.run()
