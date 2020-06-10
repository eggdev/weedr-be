import os
import praw
import dotenv

dotenv.load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_COLLECTION = os.getenv("DB_COLLECTION")
DB_NAME = os.getenv("DB_NAME")


DB_URI = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_NAME}.mongodb.net/{DB_COLLECTION}?retryWrites=true&w=majority"
