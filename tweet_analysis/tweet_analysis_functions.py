# analyse de tweet - voir le descriptif ReflexionDeGroupeV

import tweet_collection.twitter_connection_setup as connect
import tweepy
import pandas as pd
import numpy as np


#fonction de création de dataframe

def collect_to_pandas_dataframe():
   connexion = connect.twitter_setup()
   tweets = connexion.search("@EmmanuelMacron",language="fr",rpp=100)
   data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
   data['len']=np.array([len(tweet.text) for tweet in tweets])
   data['ID']=np.array([tweet.id for tweet in tweets])
   data['Date']=np.array([tweet.created_at for tweet in tweets])
   data['Source']=np.array([tweet.source for tweet in tweets])
   data['Likes']=np.array([tweet.favorite_count for tweet in tweets])
   data['RTs']=np.array([tweet.retweet_count for tweet in tweets])
   return data



#fonctions d'analyse de tweets - description dans Reflexion de groupe V
def max_retweeted(data):
    rt_max=np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))

#test :
#data=collect_to_pandas_dataframe()
#max_retweeted(data)


def max_like(data):
    like_max=np.max(data['Likes'])                          #on détermine le nombre maximum de like
    tweet=data[data.Likes == like_max].index[0]             #on selectionn ela première ligne de la dataframe obtenue après filtrage
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][tweet]))
    print("Number of likes: {}".format(like_max))

#test :
#data=collect_to_pandas_dataframe()
#max_like(data)


def le_plus_recent(data):
    max_date=np.max(data['Date'])
    tweet=data[data.Date == max_date].index[0]             #on selectionn ela première ligne de la dataframe obtenue après filtrage
    print("The most recetn tweet is: \n{}".format(data['tweet_textual_content'][tweet]))
    print("Date: {}".format(max_date))

#test :
#data=collect_to_pandas_dataframe()
#le_plus_recent(data)
