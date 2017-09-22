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
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

source_user = 'jamiejin91'

def RequestTweetParser(source_user):
    tweets = api.user_timeline(source_user)
    target_users = [tweet['entities']['user_mentions'][1]['screen_name'] for tweet in tweets if source_user != tweet['entities']['user_mentions'][1]['screen_name']]
    return target_users

def TargetVaderAnalysis(user):
    compound = []
    for i in range(25):
        try:
            public_tweets = api.user_timeline(user)
        except:
            break
        for tweet in public_tweets:
            compound.append(analyzer.polarity_scores(tweet["text"])["compound"])
    return compound

def VaderAnalysisPlot(compound):

def PostVaderPlot(vader_plot):

''' 
1. call RequestTweetParser to pull list of target users to analyze from last source id
2. loop through target users and perform:
    a. TargetVaderAnalysis takes up to 500 tweets of target user and gathers compound vader analysis
    b. VaderAnalysisPlot creates scatter plot of the target user's tweets
    c. PostVaderPlot posts the vader plot of target user to source user's twitter
3. set timer
'''