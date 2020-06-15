from flask import Flask, request
from flask_restful import Api
from flask_bcrypt import Bcrypt
from database.db import initialize_app
from database.config import DB_URI, JWT_SECRET_KEY
from flask_jwt_extended import JWTManager
from api.routes import initialize_routes
from reddit.background import initialize_background
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGODB_HOST"] = DB_URI
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_COOKIE_PATH"] = '/v1/api/'
app.config["JWT_REFRESH_COOKIE_PATH"] = '/v1/login'
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config["CORS_SUPPORTS_CREDENTIALS"] = True
app.config["CORS_ALLOW_HEADERS"] = 'Content-Type'


jwt = JWTManager(app)

api = Api(app)
bcrypt = Bcrypt(app)
CORS(app, resources={r"/v1/*": {
    "origins": "http://localhost:3000"
}})

initialize_app(app)
initialize_routes(api)
initialize_background()

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
