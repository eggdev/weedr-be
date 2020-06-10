from flask import Flask, request
from flask_restful import Api

from database.db import initialize_app
from database.config import DB_URI

from reddit.config import subreddit
from reddit.background import initialize_background

from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config["MONGODB_HOST"] = DB_URI

initialize_app(app)
initialize_routes(api)
initialize_background()

if __name__ == "__main__":
    app.run(use_reloader=False)
