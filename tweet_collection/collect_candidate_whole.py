import tweet_collection.twitter_connection_setup as connect

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 100)
    return statuses

def nb_retweet_candidat(user_id):
    """Renvoie la liste des nombres de retweets des 100 derniers tweet de user_id"""
    list_tweet=collect_by_user(user_id) #
    list_nb_retweet=[]
    for tweet in list_tweet:
        list_nb_retweet.append(tweet.retweet_count)
    return list_nb_retweet
