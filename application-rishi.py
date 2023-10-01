import tweepy
from textblob import TextBlob

# Authenticate with Twitter API
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Get tweets from a specific user
def get_user_tweets(username, count=10):
    tweets = api.user_timeline(screen_name=username, count=count)
    return [tweet.text for tweet in tweets]

# Main function to analyze sentiment of user's tweets
def main():
    username = input("Enter Twitter username: ")
    tweets = get_user_tweets(username)
    
    for i, tweet in enumerate(tweets):
        sentiment = analyze_sentiment(tweet)
        print(f'Tweet {i+1}: {tweet}')
        print(f'Sentiment: {sentiment}\n')

if __name__ == "__main__":
    main()
