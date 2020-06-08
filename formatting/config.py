import os
import dotenv
import praw

dotenv.load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD)
subreddit = reddit.subreddit("knicklejerk")
dict_fields = ('author', 'id', "name",
               "score", "num_comments", "ups", "downs", "mod_reports", "user_reports")
reported_list = []
