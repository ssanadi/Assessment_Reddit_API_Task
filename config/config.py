import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

REDDIT_CLIENT_ID = os.getenv("CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("USERNAME")
REDDIT_PASSWORD = os.getenv("PASSWORD")
REDDIT_USER_AGENT = os.getenv("USER_AGENT")