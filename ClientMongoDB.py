from pymongo import MongoClient
from pprint import pprint

client = MongoClient(
    "mongodb+srv://obukowski:cKeZ8bMmChydetKt@cluster0.oblol.mongodb.net/main?retryWrites=true&w=majority")

db = client.main
collection = db.tweet_with_model_output
serverStatusResult = db.command("serverStatus")

# pprint(serverStatusResult)

### EXAMPLE ENTRY

insert = {"id": 12345678, "model_output": 1.0}

# db.tweet_with_model_output.insert_one(insert)


### FIND ENTRY BY ID
fivestar = db.tweet_with_model_output.find_one({"id": 12345678})
print(fivestar)