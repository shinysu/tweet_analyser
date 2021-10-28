import tweepy
import config

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
tweepy_api = tweepy.API(auth)


def get_tweets(username):
    tweets = tweepy_api.user_timeline(screen_name=username,
                                      count=200,
                                      include_rts=False,
                                      tweet_mode='extended')

    return [[tweet.id, tweet.full_text, tweet.created_at] for tweet in tweets]


#if __name__ == '__main__':
#    get_tweets('shiny_su')
