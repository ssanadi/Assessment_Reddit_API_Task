from reddit.reddit_helper import upvote_post

if __name__ == "__main__":
    # You can pass a single post ID to upvote
    post_id = '1kc3vk6'
    try:
        # Upvote the post(s) using our helper method
        upvote_post(post_id)
        print(f"✅ Successfully upvoted post with ID: {post_id}")
        
    except Exception as e:
        print(f"❌ Failed to upvote post: {e}")
