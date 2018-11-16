
import tweet_collection.twitter_connection_setup as connect
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#fonction de création de dataframe

def collect_to_pandas_dataframe_keyword(keyword):         #keyword = "@EmmanuelMacron" par exemple
   connexion = connect.twitter_setup()
   tweets = connexion.search(keyword,language="fr",rpp=100)
   data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
   data['len']=np.array([len(tweet.text) for tweet in tweets])
   data['ID']=np.array([tweet.id for tweet in tweets])
   data['Date']=np.array([tweet.created_at for tweet in tweets])
   data['Source']=np.array([tweet.source for tweet in tweets])
   data['Likes']=np.array([tweet.favorite_count for tweet in tweets])
   data['RTs']=np.array([tweet.retweet_count for tweet in tweets])
   return data

def collect_to_pandas_dataframe():         #keyword = "@EmmanuelMacron" par exemple
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

#proposition de l'éconcé pour afficher les likes/retweet

data = collect_to_pandas_dataframe()
"""
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()




# essais pour comparer les likes par dates de Macron et Edouard Philippe - fait par Karine

data_Macron=collect_to_pandas_dataframe_keyword("@EmmanuelMacron")
data_Philippe=collect_to_pandas_dataframe_keyword("@EPhilippePM")

tret_Macron = pd.Series(data=data_Macron['RTs'].values, index=data_Macron['Date'])
tret_Philippe = pd.Series(data=data_Philippe['RTs'].values, index=data_Philippe['Date'])

tret_Macron.plot(figsize=(16,4), label="Retweets Macron", legend=True)
tret_Philippe.plot(figsize=(16,4), label="Retweets Philippe", legend=True)

plt.show()
"""



# essais fait par Maxime

def stat_len_et_likes(data):
    tfav = pd.Series(data=data['len'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])
    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Len", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)
    plt.show()

