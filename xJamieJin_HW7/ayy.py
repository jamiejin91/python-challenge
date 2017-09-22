# Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import config
import json
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Twitter API Keys
consumer_key = config.ck
consumer_secret = config.cs
access_token = config.at
access_token_secret = config.ats

analyzer = SentimentIntensityAnalyzer()

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Target Account
target_user = ["@bcc","@cbs","@cnn","@foxnews","@nytimes"]

df = pd.DataFrame(columns = ['account_name','tweet','time_posted','compound_score','positive_score','neutral_score','negative_score'])
x_axis = list(range(0,-100,-1))
count = 0

for user in target_user: 
    
    for i in range(5):

        public_tweets = api.user_timeline(user)

        for tweet in public_tweets:
        	
        	df.set_value(count,'account_name',tweet["user"]["screen_name"])
        	df.set_value(count,'tweet',tweet["text"])
        	df.set_value(count,'time_posted',tweet["created_at"])
        	df.set_value(count,'tweet',analyzer.polarity_scores(tweet["text"])["compound"])
        	df.set_value(count,'tweet',analyzer.polarity_scores(tweet["text"])["pos"])
        	df.set_value(count,'tweet',analyzer.polarity_scores(tweet["text"])["neu"])
        	df.set_value(count,'tweet',analyzer.polarity_scores(tweet["text"])["neg"])
        	count += 1

df.to_csv("0_newstweets.csv", encoding="utf-8", index=False)