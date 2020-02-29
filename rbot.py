import praw
import json
import credential


user = credential.get_user()
code = credential.get_code()


bot = praw.Reddit(user_agent='post_bot (by /u/lttkgpbot)',
                  client_id='52z7drAQvDQ5Fg',
                  client_secret='WjnZIXYBtekvy_TgMagXBhcV1cs',
                  username=user,
                  password=code)

subreddit = bot.subreddit('lttkgp')

with open("demo.json", 'r') as f:
	posts = json.load(f)
	for post in posts:
		subreddit.submit(title=post['title'], url=post['url'])