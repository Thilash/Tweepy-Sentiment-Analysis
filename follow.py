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


user = api.get_user("")
print(user.followers_count, user.friends_count)


unfollow = []
user_friends = user.friends()
for friend in user_friends:
    if friend.followers_count > 300 and friend.friends_count < 500:
        print(friend.screen_name)
        relationship = api.create_friendship(friend.screen_name)
        unfollow.append(friend.screen_name)

print(unfollow)

time.sleep(20)

for person in unfollow:
    api.destroy_friendship(person)
