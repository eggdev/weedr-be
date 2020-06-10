from flask import Flask, request
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask_restful import Api
from database.db import initialize_app
from database.config import DB_URI
from reddit.config import subreddit
from reddit.app import collect_recently_reported_users
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config["MONGODB_HOST"] = DB_URI

collect_recently_reported_users()
initialize_app(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run()
