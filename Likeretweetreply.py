import tweepy
import webbrowser
import time
import pandas as pd

callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pint_input = input("What is the pin?")
auth.get_access_token(user_pint_input)


api = tweepy.API(auth)
me = api.me()
print(me.screen_name)

status_obj = api.get_status("1305846205222539265")
print(status_obj.text)

api.retweet(1305846205222539265)
api.create_favorite(1305846205222539265)

user = api.get_user("Stretched")
user_timeline = user.timeline()
status_obj_id = user_timeline[13].id
print(status_obj_id)


#og_tweet = api.get_status("1305846205222539265")
#print(og_tweet.user.screen_name, og_tweet.id)
#my_reply = api.update_status(f"@{og_tweet.user.screen_name}out opening twitter",og_tweet.id)
#print(my_reply.user.screen_name)
