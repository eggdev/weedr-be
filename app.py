from flask import Flask, request, Response
# from models import User
from db_config import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/redditor_reports'
}

initialize_db(app)


@app.route("/users")
def get_users():
    return {"user": "username"}


@app.route("/users", methods=['POST'])
def add_user():
    print(request.get_json())
    return {"body": "none"}, 200
    # body = request.get_json()
    # user = User(**body).save()
    # id = user.id
    # return {"id": str(id)}, 200


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    print(id)
    return "", 200
    # body = request.get_json()
    # # Spread operator in python == **
    # User.objects.get(id=id).update(**body)
    # return "", 200


@app.route("/users/<id>", methods=["DELETE"])
def remote_user(id):
    print(id)
    return "", 200
    # User.objects.get(id=id).delete()
    # return "", 200


app.run()
