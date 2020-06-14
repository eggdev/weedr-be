#  Capture all reported items for this subreddit
import datetime
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                set_access_cookies,
                                set_refresh_cookies,
                                unset_jwt_cookies,
                                get_jwt_identity)
from database.User.models import User
from reddit.config import reddit


class Signup(Resource):
    def post(self):
        body = request.get_json()
        username = body["username"].lower()
        try:
            User.objects.get(username=username)
            resp = make_response({"found": "User already exists"}, 201)
            return resp
        except User.DoesNotExist:
            new_user = User(username=username)
            new_user.password = body["password"]
            new_user.hash_password()
            # Generate new user object with password
            new_user.save()
            resp_user = new_user.generate_return_object()
            resp = make_response(resp_user, 200)
            access_token = create_access_token(
                identity=str(new_user.username)
            )
            refresh_token = create_refresh_token(
                identity=str(new_user.username)
            )
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp


class Login(Resource):
    def post(self):
        body = request.get_json()
        username = body.get('username').lower()
        try:
            user = User.objects.get(username=username)
            # Checking if users password is correct
            authorized = user.check_password(body.get('password'))
            if not authorized:
                resp = make_response({
                    "error": "Username or password invalid",
                    "logged_in": False
                }, 401)
                return resp
            access_token = create_access_token(
                identity=str(user.username)
            )

            refresh_token = create_refresh_token(
                identity=str(user.username)
            )
            resp_user = user.generate_return_object()
            resp = make_response(resp_user, 201)
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp
        except User.DoesNotExist:
            resp = make_response({"logged_in": False}, 403)
            return resp


class Logout(Resource):
    def post(self):
        resp = make_response({"logged_in": False}, 200)
        unset_jwt_cookies(resp)
        return resp


class UserAccount(Resource):
    @jwt_required
    def get(self):
        curr = get_jwt_identity()
        user = User.objects.get(username=curr)
        return_obj = user.generate_return_object()
        resp = make_response(return_obj, 200)
        return resp

    @jwt_required
    def put(self):
        curr = get_jwt_identity()
        body = request.get_json()
        code = body["code"]
        refresh_token = reddit.auth.authorize(code)
        reddit_un = reddit.user.me().name
        user = User.objects.get(username=curr)
        new_accounts = user.add_account(reddit_un, refresh_token)
        user.update(reddit_accounts=new_accounts)
        resp = make_response(user, 200)
        return resp


class RedditAuth(Resource):
    @jwt_required
    def get(self):
        auth_url = reddit.auth.url(scope_list, 'state_val', 'permanent')
        return auth_url, 200
