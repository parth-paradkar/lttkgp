import praw
from reddit.keys import *
from urllib.parse import parse_qs, urlparse

reddit = praw.Reddit(client_id=APP_ID, client_secret=APP_SECRET, user_agent=USER_AGENT)
subreddit = reddit.subreddit("lttkgp")

def split_url(url):
    return parse_qs(urlparse(url).query)

def getPosts():
    posts = []
    for submission in subreddit.top():
        post = {
                "post_id": submission.id,
                "author": {
                    "id": submission.author.id,
                    "name": submission.author.name
                    },
                "score": submission.score,
                "title": submission.title,
                "url": submission.url,
                "url_params": split_url(submission.url)
                }
        posts.append(post)
    return posts


if __name__ == '__main__':
    pass
