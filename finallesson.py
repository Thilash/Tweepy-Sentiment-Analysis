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

query = "McMaster"
for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(25)):
    print(i, status.text,status.author.screen_name)
    print("\n")

query_username = "Django"
