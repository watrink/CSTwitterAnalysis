# Objectif: comprendre un peu mieux les fonctions faites par les autres



import tweepy
import tweet_collection.twitter_connection_setup as connect
import numpy as np
import pandas as pd


"""
# test avce la fonction collect_by_user pour comprendre l'architecture des status

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 100)
    for status in statuses:
        print(status.text)
    return statuses

#1976143068
"""





"""
# test sur le fonctionnement pour ouvrir des fichiers .txt

mon_fichier = open("C:/Users/Actif/PycharmProjects/TwitterPredictor/CandidatData/hashtag_candidate_n.txt", "r")
contenu = mon_fichier.read()
contenu=contenu.split("\n")
long=len(contenu)
user=contenu[:long-1]    #
print(type(user))

print(user)
mon_fichier.close()
"""

# test sur Panda

liste=[1,3,5,7]
test_panda=pd.Series(liste,index=['a','b','c','d']) #il faut maintentant l'afficher pur vraiment comprendre


