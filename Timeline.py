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

#my_timeline = api.home_timeline()
#for status in my_timeline:
#    print(status.text)
#    print("\n")


user = api.get_user("tinybbycutiegrl")
user_timeline = user.timeline()
count = 0
for x in user_timeline:
    print(x.text)
    print("\n")
    count = count + 1
    if count > 2: break
    
    
