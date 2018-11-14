
#fonction demandée en II 4 écrite par Maxime, description dans le fichier Word ReflexionDeGroupeII4

import tweepy
import tweet_collection.twitter_connection_setup as connect


from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True
def collect_by_streaming():
    connexion = connect.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])


