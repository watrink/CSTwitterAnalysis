#Objectif: prise en main de TextBlob



import tweet_collection.twitter_connection_setup as connect
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer


#il faut d'abord collecter les tweets

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 10)
    for status in statuses:
        print(status.text)
    return statuses


def collect_to_pandas_dataframe():
   connexion = connect.twitter_setup()
   tweets = collect_by_user(25073877)
   data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
   data['len']=np.array([len(tweet.text) for tweet in tweets])
   data['ID']=np.array([tweet.id for tweet in tweets])
   data['Date']=np.array([tweet.created_at for tweet in tweets])
   data['Source']=np.array([tweet.source for tweet in tweets])
   data['Likes']=np.array([tweet.favorite_count for tweet in tweets])
   data['RTs']=np.array([tweet.retweet_count for tweet in tweets])
   return data



def get_text_only(data, texte_initial): #fonction qui transforme les textes des tweets en string
    array=np.array(pd.DataFrame(data,columns=['tweet_textual_content']))
    for tweet in array:
        texte_initial+=tweet
    return texte_initial[0]




def extract_voc_tweet(texte): #fonction qui permet d'extraire le vocabulaire le plus important et revelateur d'un tweet. la fonction renvoie tous les mots utilisés (sauf les pronoms, conjonction de coordiation et autre petits mots outils et ainsi qu eleur nombre. A partir de ça nous pensions faire des comparaisons et des analyses de sentiments
    voc={}
    content=TextBlob(texte)
    words=content.tags
    class_to_supress=['C','W','P','I','D','R']
    for word in words:                #il  nous faut enlever certains mots, 1) ceux qui contiennent https etc
        if (word[0][:3]!='htt') and (len(word[0])>2) and (word[1][0] not in class_to_supress):
            if word[1][0]=='V':
                word_only=Word(word[0]).lemmatize('v')
                #if not (word[0] in ['be','have','do','go','make','will','want']):
            if word[1]=='NN':
                word_only=Word(word[0]).singularize()
            word_only=word[0]
            if word_only not in voc.keys():
                voc[word_only]=1
            else:
                voc[word_only]+=1
    return voc


"""
# tests
data=collect_to_pandas_dataframe()
texte=get_text_only(data,'')
voc=extract_voc_tweet(texte)
"""

### Analyse des sentiments

def analyse_tweet(data):
   array=np.array(pd.DataFrame(data,columns=['tweet_textual_content']))
   pos_tweets=[]
   neu_tweets=[]
   neg_tweets=[]
   for tweet in array:        #tris des tweets en fonction de leur 'sentiment'
      text=tweet[0]
      blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
      if blob.sentiment[0]=='pos':
         pos_tweets.append(blob)
      if blob.sentiment[0]=='neu':
         neu_tweets.append(blob)
      if blob.sentiment[0]=='neg':
         neg_tweets.append(blob)

   print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
   print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
   print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))

"""
# tests
data=collect_to_pandas_dataframe()
analyse_tweet(data)


# les testes renvoient des choses assez bizarre parce que le sentiment de "I hate you" est 'pos'
"""

