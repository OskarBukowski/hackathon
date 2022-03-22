from pymongo import MongoClient


class MongoDBClient:
    def __init__(self):
        self.db = MongoClient(
            "mongodb+srv://obukowski:cKeZ8bMmChydetKt@cluster2.l4m5p.mongodb.net/main?retryWrites=true&w=majority").main.tweet_with_model_output

    def update_db(self, attribute):
        return self.db.insert_one(attribute)

    def read_db(self, attribute):
        return self.db.find_one(attribute)

    def drop_document(self, attribute):
        return self.db.dropIndex(attribute)

    def drop_all_document(self):
        return self.db.dropIndexes("*")


