import os
import praw
import dotenv

dotenv.load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
SUBREDDIT = os.getenv("SUBREDDIT")
DB_NAME = os.getenv("DB_NAME")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

DB_URI = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_NAME}.mongodb.net/dev"
