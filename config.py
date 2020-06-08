import os
import dotenv

dotenv.load_dotenv()

API_SECRET_KEY = os.getenv("API_SECRET_KEY")
PERSONAL_USE_SCRIPT = os.getenv("PERSONAL_USE_SCRIPT")
USER_AGENT = os.getenv("USER_AGENT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
