import praw
from config.config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_PASSWORD, REDDIT_USERNAME

# Initialize Reddit instance with script-type OAuth (allows read/write actions)
def get_reddit_client():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD
    )

def get_latest_posts(subreddit_name:str, limit:int=1):
    """
    Fetches the latest posts from a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to fetch posts from.
        limit (int): Number of posts to retrieve (default is 1).

    Returns:
        list: A list of dictionaries.
    """
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)
    return list(subreddit.new(limit=limit))

def upvote_post(post_id:str):
    """
    Upvotes Reddit posts.

    Args:
        post_id (str): post ID to upvote.
    """
    reddit = get_reddit_client()
    submission = reddit.submission(id=post_id)
    submission.upvote()
