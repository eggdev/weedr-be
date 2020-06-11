from flask import Flask, request
from flask_restful import Api
from flask_bcrypt import Bcrypt
from database.db import initialize_app
from database.config import DB_URI, JWT_SECRET_KEY
from flask_jwt_extended import JWTManager
from api.routes import initialize_routes
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGODB_HOST"] = DB_URI
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY


api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app, resources={r"/v1/*": {"origins": "*"}})

initialize_app(app)
initialize_routes(api)


# initialize_background()
if __name__ == "__main__":
    app.run()
