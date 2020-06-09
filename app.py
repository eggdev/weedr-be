from flask import Flask, request, Response
# from models import User
from db_config import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/redditor_reports'
}

initialize_db(app)


@app.route("/")
def hello():
    return {"hello": "world"}

# @app.route("/users")
# def get_users():
#     users = User.objects().to_json()
#     return Response(users, mimetype="application/json", status=200)


# @app.route("/users", methods=['POST'])
# def add_user():
#     body = request.get_json()
#     user = User(**body).save()
#     id = user.id
#     return {"id": str(id)}, 200


# @app.route("/users/<id>", methods=["PUT"])
# def update_user(id):
#     body = request.get_json()
#     # Spread operator in python == **
#     User.objects.get(id=id).update(**body)
#     return "", 200


# @app.route("/users/<id>", methods=["DELETE"])
# def remote_user(id):
#     User.objects.get(id=id).delete()
#     return "", 200


app.run()
