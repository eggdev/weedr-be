import os
import dotenv
import praw

dotenv.load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

SUBREDDIT = os.getenv("SUBREDDIT")

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD)

subreddit = reddit.subreddit(SUBREDDIT)

dict_fields = ("author",
               "id",
               "name",
               "score",
               "ups",
               "num_comments",
               "downs",
               "mod_reports",
               "user_reports")
