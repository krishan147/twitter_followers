import time
import tweepy

class Twitter():

    def __init__(self,tw_handle):

        self.tw_handle = tw_handle

        #TWITTER AUTHENTICATION DETAILS

        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        #TWITTER API - FOLLOWERS

        api = tweepy.API(auth)
        user = api.get_user(tw_handle)

        print user._json['followers_count']
        time.sleep(3)

#Twitter('elonmusk')
