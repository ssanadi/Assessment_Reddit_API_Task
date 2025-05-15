from reddit.reddit_helper import comment_on_post
from faker import Faker
import random

def generate_reddit_comment():
    """
    Generates a realistic Reddit-style comment using Faker.
    
    Returns:
        str: A realistic Reddit comment
    """
    fake = Faker()
    
    # Different types of comment templates
    comment_templates = [
        # Opinion-based comments
        "I think {topic} is really {adjective}. {sentence}",
        "In my experience, {topic} has been {adjective}. {sentence}",
        
        # Question-based comments
        "Has anyone else noticed that {topic}? {sentence}",
        "What are your thoughts on {topic}? {sentence}",
        
        # Discussion-based comments
        "This reminds me of {topic}. {sentence}",
        "I've been thinking about {topic} lately. {sentence}",
        
        # Agreement/disagreement comments
        "I completely agree with this! {sentence}",
        "While I see your point, I think {sentence}",
        
        # Personal experience comments
        "I had a similar experience with {topic}. {sentence}",
        "This happened to me when {sentence}"
    ]
    
    # Generate random components for the comment
    topic = fake.word()
    adjective = fake.word()
    sentence = fake.sentence()
    
    # Select a random template and fill it
    template = random.choice(comment_templates)
    comment = template.format(
        topic=topic,
        adjective=adjective,
        sentence=sentence
    )
    
    # Add some Reddit-style formatting randomly
    if random.random() < 0.3:  # 30% chance to add formatting
        formatting_choices = [
            f"**{comment}**",  # Bold
            f"*{comment}*",    # Italic
            f"> {comment}",    # Quote
            f"EDIT: {comment}" # Edit
        ]
        comment = random.choice(formatting_choices)
    
    return comment

if __name__ == "__main__":
    # Example post ID
    post_id = '1kc3vk6'  # Replace with actual post ID
    
    try:
        # Generate and add a realistic comment
        comment_text = generate_reddit_comment()
        print(f"Generated comment: {comment_text}\n")
        
        # Add comment to the post
        comment = comment_on_post(post_id, comment_text)
        print(f"✅ Successfully added comment to post {post_id}")
        print(f"Comment ID: {comment.id}")
        
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Failed to add comment: {e}") 