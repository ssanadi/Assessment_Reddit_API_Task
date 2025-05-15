import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("USERNAME")
REDDIT_PASSWORD = os.getenv("PASSWORD")
REDDIT_USER_AGENT = os.getenv("USER_AGENT")

# Retry settings
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))  # Default to 3 retries
RETRY_DELAY = int(os.getenv('RETRY_DELAY', '2'))  # Default to 2 seconds delay