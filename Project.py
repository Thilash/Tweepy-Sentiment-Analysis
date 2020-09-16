import tweepy
import webbrowser
import time
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List

callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pint_input = input("What is the pin?")
auth.get_access_token(user_pint_input)


api = tweepy.API(auth)
me = api.me()
print(me.screen_name)

def get_tweets(keyword: str) -> List[str]:
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(15):
        tweets.append(tweet.full_text)
    return tweets

def clean(tweets: List[str]) -> List[str]:
    clean_tweets = []
    for tweet in tweets:
        clean_tweets.append(p.clean(tweet))
    return clean_tweets

def sentiment(tweets: List[str]) -> List[float]:
    review = []
    for tweet in tweets:
        blob = TextBlob(tweet)
        review.append(blob.sentiment.polarity)
    return review

def my_mean(values: List[float]) -> int:
   sum, n = 0, 0
   for x in values:
      sum += x
      n += 1
   return float(sum)/n

def avg_sentiment(keyword) -> int:
    tweets = get_tweets(keyword)
    clean_tweets = clean(tweets)
    sentimental = sentiment(clean_tweets)
    avg = my_mean(sentimental)
    return avg


print("what do you want to compare? ")
first = input()
print("whats the second thing? ")
second = input()

score1 = avg_sentiment(first)
score2 = avg_sentiment(second)
print(score1, score2)

if score1 > score2:
    print(first + " is better than " + second)
else:
    print(second +" is better than "+ first)
    
