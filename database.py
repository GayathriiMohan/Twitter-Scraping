import pymongo
def insert_to_mongo(tweets):
    def connect_to_mongo():
        client = pymongo.MongoClient(
            "mongodb+srv://Gayathri:1234@gayathri.mzcfyox.mongodb.net/?retryWrites=true&w=majority")
        db = client["LIC Corporation_Tweets_DB"]
        tweets_collection = db["LIC Corporation_Tweets_"]
        return tweets_collection