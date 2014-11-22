import tweepy

auth = tweepy.OAuthHandler("esIjQxZqM92UPtYIjSRb0xqjX", "jrflNn5OyF12D9EN1eEF4UFdZLVsHThb7bEIGF69wAInqlhLWx")
auth.set_access_token("19103984-qvH0nDhIuLWX7b0LVIsLIOr4UmOsNwVRSvhzbZcHA", "A5jV0B6PA7ktLBt3FnbRPJ1OKZuYVstWFroYHjuLfLNST")

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet.text

user = api.get_user('usmanghani')

print user.screen_name
print user.followers_count


for friend in user.friends():
    print friend.screen_name


