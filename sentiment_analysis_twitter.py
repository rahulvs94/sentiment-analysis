import sys
import tweepy
from textblob import TextBlob

print("The arguments are: " , list(sys.argv)[1:])

consumer_key = 'JN8o9LIQlGqGQlJcloxANAMzx'
consumer_secret = 'M4ewNVCaWzlGWMC5WPrIdXHR1aFl2gqj36P9JJw32cjQ6WaprG'

access_token = '1095878029635710976-c5wMnNnQhH31QzUFr2YgTWq9rdpjzI'
access_token_secret = '30WrHu5ESrvBV1FvrzMP4dF8eDLeyjxIZUhVUBFH9iKfM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(sys.argv[1:])

for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
