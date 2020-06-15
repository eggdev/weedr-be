import datetime
import praw
import requests
import json
from pprint import pprint
from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import Document, StringField, ListField
from reddit.config import generate_praw_instance


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    refresh_token = StringField(required=True)
    reddit_accounts = ListField(required=False)
    moderating = ListField(required=False)

    def single_user_info(self):
        acc = self.reddit_accounts[0]
        return {"token": acc["refresh_token"], "un": acc["username"]}

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_account(self, username, refresh_token):
        self.reddit_accounts.append(
            {"username": username, "refresh_token": refresh_token}
        )
        return self.reddit_accounts

    def update_refresh_token(self):
        token = self.single_user_info()["token"]
        return generate_praw_instance(token)

    def generate_moderated_subs(self, subs_list):
        clean = []
        for sub in subs_list:
            clean.append(sub.display_name)
        self.moderating = clean

    def generate_return_object(self):
        token = self.single_user_info()["token"]
        un = self.single_user_info()["un"]
        reddit = generate_praw_instance(token)
        moderated = reddit.redditor(un).moderated()
        self.refresh_token = token
        self.generate_moderated_subs(moderated)
        self.save()
        return {
            "username": self.username,
            "reddit_accounts": self.reddit_accounts,
            "moderating": self.moderating
        }
