import praw
import pandas as pd
import datetime as dt
import json
import pprint
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD
from helpers import aggregate_and_format_reddit_data

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD)

subreddit = reddit.subreddit("knicklejerk")
reported_list = []

dict_fields = ('author', 'id', "name",
               "score", "num_comments", "ups", "downs", "mod_reports", "user_reports")


def get_reported_data(sub):
    # format and append all reported comments
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("comments"), dict_fields),)

    # format and append all reported submissions
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("submissions"), dict_fields))


get_reported_data(subreddit)
with open("reported.json", "w") as json_file:
    json.dump(reported_list, json_file)
