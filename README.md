# Reddit API Task - TheSoul Publisher Assessment 

## Objective

This script demonstrates the use of the Reddit API (via PRAW) to:

1. Authenticate using OAuth.
2. Fetch the latest 5 posts from a specified subreddit.
3. Upvote a given Reddit post.
4. Add comments to posts with realistic content.

## Setup Instructions

### 1. Create a Reddit App
- Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
- Click "Create App" or "Create Another App"
- Set:
 1. name: Your app name
 2. type: script
 3. redirect URI: http://localhost
- Save your Client ID and Client secret

### 2. Set Up Environment Variables
```env
CLIENT_ID=<your_client_id>
CLIENT_SECRET=<your_client_secret>
USERNAME=<your_reddit_username>
PASSWORD=<your_reddit_password>
USER_AGENT=script:your_app_name:v1.0 (by /u/<your_reddit_username>)
MAX_RETRIES=3
RETRY_DELAY=2
```
Never commit your .env to version control.

### 3. Create Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. How to Run
### Fetch Latest Posts
```bash
python reddit_post_fetcher.py
```

### Upvote Post
```bash
python reddit_upvote_post.py
```

### Add Comment
```bash
python reddit_comment.py
```

## Features
- OAuth authentication with Reddit
- Fetch latest posts from any subreddit
- Upvote post
- Add realistic comments using Faker
- Automatic retry mechanism with configurable settings
- Modular and extensible code
- Error handling with helpful messages

## Retry Mechanism
The script includes an automatic retry mechanism that:
- Handles rate limits automatically
- Configurable retry attempts (MAX_RETRIES)
- Configurable delay between retries (RETRY_DELAY)
- Exponential backoff strategy

## Comment Generation
The comment system:
- Generates realistic Reddit-style comments
- Includes various comment templates
- Adds random Reddit formatting
- Handles errors gracefully

## 📞 Contact
- Author: SaifAli Umar Sanadi
- Email: sanadi.saifali.7@gmail.com
- GitHub: [ssanadi](https://github.com/ssanadi)

