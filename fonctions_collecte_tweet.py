import tweet_collection.twitter_connection_setup as connect
import tweepy

def collect():
    connexion = connect.twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=1)
    for tweet in tweets:
        print(tweet.text)

# API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])



def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 20)
    for status in statuses:
        print(status.text)
    return statuses


# user_id d'emmanuel Macron  1976143068
# user_id de Trump 25073877


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


