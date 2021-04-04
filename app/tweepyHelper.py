import os
from dotenv import load_dotenv
import tweepy


class TweepyHelper:
    __TweepyApi = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if TweepyHelper.__TweepyApi == None:
            TweepyHelper()
        return TweepyHelper.__TweepyApi

    def __init__(self):
        """ Virtually private constructor. """
        if TweepyHelper.__TweepyApi != None:
            raise Exception("Something went wrong")
        else:
            load_dotenv(override=True)
            TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
            TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
            tweepyAuth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
            TweepyHelper.__TweepyApi = tweepy.API(tweepyAuth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    @staticmethod
    def fetchTweet(amount=10):
        tweet_list = []
        for status in tweepy.Cursor(TweepyHelper.__TweepyApi.search, q='#covid19', count=100000, lang='en', tweet_mode='extended').items(100000):
            if not status._json['full_text'].startswith('RT'):
                tweet_list += [status._json]
            if(amount <= len(tweet_list)):
                break
        return tweet_list
