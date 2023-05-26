import tweepy
import json

with open('src\\private\\accesstokens.json') as file:
    data = json.load(file)

apiKey = data['api-key']
apiKeySecret = data['api-key-secret']

bearerToken = data['bearer-token']

accessToken = data['access-token']
accessTokenSecret = data['access-token-secret']

def client():
    client = tweepy.Client(
        bearer_token=bearerToken,
        consumer_key=apiKey,
        consumer_secret=apiKeySecret,
        access_token=accessToken,
        access_token_secret=accessTokenSecret
    )

    return client

def tweet(api: tweepy.Client, message: str):
    try:
        api.create_tweet(text=message)
        print("Tweeted successfully.")
    except tweepy.TweepyException as e:
        print(f"Tweet was unsuccessful: {e}")