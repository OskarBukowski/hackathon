from pymongo import MongoClient
from pprint import pprint

client = MongoClient(
    "mongodb+srv://obukowski:cKeZ8bMmChydetKt@cluster0.oblol.mongodb.net/main?retryWrites=true&w=majority")

db = client.main
collection = db.tweet_with_model_output

### EXAMPLE ENTRY

insert = {"id": 12345678, "model_output": 1.0}

# db.tweet_with_model_output.insert_one(insert)


### FIND ENTRY BY ID

response = db.tweet_with_model_output.find_one({"id": 12345678})


# print(response)


class MongoDBClient:
    def __init__(self):
        self.db = MongoClient(
            "mongodb+srv://obukowski:cKeZ8bMmChydetKt@cluster0.oblol.mongodb.net/main?retryWrites=true&w=majority").main.tweet_with_model_output

    def update_db(self, attribute):
        return self.db.insert_one(attribute)

    def read_db(self, attribute):
        return self.db.find_one(attribute)


id = {"id": 12345678}

d = MongoDBClient().read_db(id)

print(d)

# r = {'_id': ObjectId('6235ffdd6c156c9cc5707512'), 'id': 12345678, 'model_output': 1.0}

response = {d['id']: d['model_output']}

print(type(response))