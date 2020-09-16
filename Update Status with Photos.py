import tweepy
import webbrowser
import time


callback_uri = 'oob'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)

redirect_url = auth.get_authorization_url()

webbrowser.open(redirect_url)

user_pint_input = input("What is the pin?")

auth.get_access_token(user_pint_input)


api = tweepy.API(auth)
me = api.me()
print(me.screen_name)

img_obj = api.media_upload("try.png")

new_status = api.update_status("yoj?", media_ids=[img_obj.media_id_string])
new_status.destroy()


