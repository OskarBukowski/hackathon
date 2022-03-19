from pymongo import MongoClient
from pprint import pprint


client = MongoClient("mongodb+srv://obukowski:cKeZ8bMmChydetKt@cluster0.oblol.mongodb.net/test?retryWrites=true&w=majority")
db = client.admin


serverStatusResult = db.command("serverStatus")

pprint(serverStatusResult)