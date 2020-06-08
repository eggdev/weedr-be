import praw
import pandas as pd
import datetime as dt
import json
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD)

subreddit = reddit.subreddit("knicklejerk")
reported_list = []


def get_reported_data(sub):
    # go through all reported comments
    reported_comments = sub.mod.reports("comments")
    for comment in reported_comments:
        comment_fields = ('body', 'id')
        to_dict = vars(comment)
        # Configure their object
        sub_dict = {field: to_dict[field] for field in comment_fields}
        sub_dict["author"] = serialized_author = str(comment.author)
        # Add to list of collected data
        reported_list.append(sub_dict)

    reported_posts = sub.mod.reports("submissions")
    for post in reported_posts:
        post_fields = ('title', 'id')
        to_dict = vars(post)
        # Configure their object
        sub_dict = {field: to_dict[field] for field in post_fields}
        sub_dict["author"] = serialized_author = str(post.author)
        # Add to list of collected data
        reported_list.append(sub_dict)


get_reported_data(subreddit)

with open("comments.json", "w") as json_file:
    json.dump(reported_list, json_file)
