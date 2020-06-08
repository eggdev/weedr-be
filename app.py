#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
from config import API_SECRET_KEY, PERSONAL_USE_SCRIPT, USER_AGENT, USERNAME, PASSWORD

reddit = praw.Reddit(
    client_id=API_SECRET_KEY,
    client_secret=PERSONAL_USE_SCRIPT,
    user_agent=USER_AGENT)

subreddit = reddit.subreddit("NYKnicks")

print(subreddit)
