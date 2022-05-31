import tweepy as tw
import pandas as pd

print(tw.__version__)

api_key = 'I1sBFlDanPD4zVZFCSJqwCy1R'
api_secret_key = '7A7jcG35UU1YjQGcukjzBkm4Qn0UD8XJuqPCS8P9FTH9cgvpao'
access_token = '41781444-ChLbUnnsqOLg9hz0612ECM5qTcZkS32Scjic3BJIc'
access_token_secret = 'tjy76DUzNQf1ET5bvOgaFm5g4zxa6C7p51rJ4RTvSAOQ5tjy76DUzNQf1ET5bvOgaFm5g4zxa6C7p51rJ4RTvSAOQ5'
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

key_words = "pos do arthur"
search_result = tw.Cursor(api.search_tweets, q=key_words, lang="pt", truncated=True).items(10)
crawling_result = [api.get_status(data.id, tweet_mode="extended") for data in search_result]
tweet_list = [[status.user.screen_name, status.full_text, status.retweet_count, status.favorite_count, status.geo, status.source, status.user.verified, status.author.created_at, status.author.default_profile_image, status.author.default_profile, status.user.statuses_count, status.user.friends_count, status.user.followers_count, status.user.location] for status in crawling_result]

tweet_df = pd.DataFrame(data = tweet_list, columns=["username", "tweet", "retweet_count", "like_count", "location", "device", "verified_status", "acc_creation_date","no_profile_pic", "no_bio", "tweets_count", "followings_count", "followers_count", "user_location"])

tweet_df.to_csv(r'Data_Collection_Result.csv', index=False)