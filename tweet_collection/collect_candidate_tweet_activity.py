
#fonction demandée en II 4 écrite par Maxime, description dans le fichier Word ReflexionDeGroupeII4

import tweet_collection.twitter_connection_setup as connect

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 10)
    """for status in statuses:
        print(status.text)"""
    return statuses

def nb_retweet_candidat(user_id):
    """Renvoie la liste des nombres de retweets des 100 derniers tweet de user_id"""
    #Modifie la sortie de la fonction collect_by_user
    tweet_original=collect_by_user(user_id) #
    tweet_modif=str(tweet_original)
    tweet=tweet_modif.split("\'")
    list_nb_retweet=[]
    while "retweet_count" in tweet: #tant qu'il y a des nombres de retweet, ajoute le nombre et enlève la reference au nombre de retweets
        i=tweet.index("retweet_count")
        list_nb_retweet.append(int(tweet[i+1][2:-2]))
        tweet.remove("retweet_count")
    return list_nb_retweet



