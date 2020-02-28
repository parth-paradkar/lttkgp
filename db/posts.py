from pymongo import MongoClient
from reddit.connect import getPosts

client = MongoClient()
db = client["lttkgp"]
collection = db.reddit_posts

def add_post(post):
    if(len(list(collection.find({"post_id": post["post_id"]}))) == 0):
        return collection.insert_one(post).inserted_id
    return False

for post in getPosts():
    add_post(post)



