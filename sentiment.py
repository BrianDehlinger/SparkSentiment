import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch

#import twitter keys and tokens
from config import *

# instance of elasticsearch is created as 
elasticsearch = Elasticsearch()

class TweetStreamListener(StreamListener):


    def on_data(self, data):
        
        #decodes the json
        tweet_dictionary = json.loads(data)
        print(tweet_dictionary['user']['location'])
        #Retrieves tweet data into object tweet by using TextBlob
        tweet = TextBlob(tweet_dictionary["text"])

        #determine if sentiment is positive, negative, or netural

        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        #output sentiment
        print(tweet_dictionary["text"])

        elasticsearch.index(index="nationalparks",
                 doc_type="test-type",
                 body={"author": tweet_dictionary["user"]["screen_name"],
                       "date": tweet_dictionary["created_at"],
                       "message": tweet_dictionary["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True
    

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    listener = TweetStreamListener()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)

    with open("nationalparks.txt") as file:
        nationalparks = file.readlines()
        nationalparks = [item.strip() for item in nationalparks]

    stream.filter(track=nationalparks)
