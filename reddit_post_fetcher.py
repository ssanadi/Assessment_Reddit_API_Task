from reddit.reddit_helper import get_latest_posts

if __name__ == "__main__":
    
    # Define the target subreddit (e.g., 'python')
    subreddit_name = "python"
    limit=5

    try:
        # Fetch the latest 5 posts
        posts = get_latest_posts(subreddit_name,limit)
        print(f"\n ✅ Latest {limit} posts for target subreddit '{subreddit_name}':\n")

        # Display each post's title, author, and score (upvote count)
        for post in posts:
            print(f"- Title: {post.title}")
            print(f"- Author: {post.author}")
            print(f"- Upvotes: {post.score}\n")
            print("-" * 40)

    except Exception as e:
        print(f"❌ Failed to fetch posts: {e}")