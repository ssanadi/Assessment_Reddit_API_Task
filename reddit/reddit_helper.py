import praw
import time
from functools import wraps
from prawcore.exceptions import TooManyRequests
from config.config import (
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, 
    REDDIT_PASSWORD, REDDIT_USERNAME, MAX_RETRIES, RETRY_DELAY
)

def handle_retry():
    """
    Simple decorator to handle retries with configurable settings.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            
            while retries < MAX_RETRIES:
                try:
                    return func(*args, **kwargs)
                except TooManyRequests as e:
                    retries += 1
                    if retries == MAX_RETRIES:
                        raise Exception(f"Rate limit exceeded after {MAX_RETRIES} retries. Please try again later.")
                    
                    print(f"Rate limit hit. Retrying in {RETRY_DELAY} seconds... (Attempt {retries}/{MAX_RETRIES})")
                    time.sleep(RETRY_DELAY)
            
            return None
        return wrapper
    return decorator

# Initialize Reddit instance with script-type OAuth (allows read/write actions)
def get_reddit_client():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD
    )

@handle_retry()
def get_latest_posts(subreddit_name:str, limit:int=1):
    """
    Fetches the latest posts from a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to fetch posts from.
        limit (int): Number of posts to retrieve (default is 1).

    Returns:
        list: A list of dictionaries.
        
    Raises:
        Exception: If rate limit is exceeded after max retries
    """
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)
    return list(subreddit.new(limit=limit))

@handle_retry()
def upvote_post(post_id:str):
    """
    Upvotes Reddit posts.

    Args:
        post_id (str): post ID to upvote.
        
    Raises:
        Exception: If rate limit is exceeded after max retries
    """
    reddit = get_reddit_client()
    submission = reddit.submission(id=post_id)
    submission.upvote()

@handle_retry()
def comment_on_post(post_id: str, comment_text: str):
    """
    Adds a comment to a Reddit post.

    Args:
        post_id (str): The ID of the post to comment on.
        comment_text (str): The text content of the comment.

    Returns:
        praw.models.Comment: The created comment object.

    Raises:
        Exception: If rate limit is exceeded after max retries
        ValueError: If comment_text is empty or None
    """
    if not comment_text or not comment_text.strip():
        raise ValueError("Comment text cannot be empty")

    reddit = get_reddit_client()
    submission = reddit.submission(id=post_id)
    comment = submission.reply(comment_text)
    return comment
