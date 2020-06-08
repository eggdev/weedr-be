import praw
import pandas as pd
import datetime as dt
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD)

subreddit = reddit.subreddit("knicklejerk")

reported_comments = subreddit.mod.reports("comments")
reported_posts = subreddit.mod.reports("submissions")

for comment in reported_comments:
    # for reported comment in modqueue:
    # get the reported users name
    print(f"Comment: {comment.author}")

for post in reported_posts:
    # for reported post in modqueue:
    # get the reported users name
    print(f"Post: {post.author}")
