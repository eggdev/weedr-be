from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"user_name": "clydeedgar",
     "reports": [
         {"title": "butts"}
     ]
     },
    {"user_name": "schildkrotes",
     "reports": [
         {"title": "carlton"}
     ]
     }
]


@app.route("/users")
def get_all_users():
    return jsonify(users)


app.run()
