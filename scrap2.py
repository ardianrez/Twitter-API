import tweepy as tw
import pandas as pd

api_key = 'I1sBFlDanPD4zVZFCSJqwCy1R'
api_secret_key = '7A7jcG35UU1YjQGcukjzBkm4Qn0UD8XJuqPCS8P9FTH9cgvpao'
access_token = '41781444-ChLbUnnsqOLg9hz0612ECM5qTcZkS32Scjic3BJIc'
access_token_secret = 'tjy76DUzNQf1ET5bvOgaFm5g4zxa6C7p51rJ4RTvSAOQ5tjy76DUzNQf1ET5bvOgaFm5g4zxa6C7p51rJ4RTvSAOQ5'

auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)