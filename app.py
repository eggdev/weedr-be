import praw
import pandas as pd
import datetime as dt
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT)

for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)
