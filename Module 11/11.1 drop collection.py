import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
database=conn["Python"]
collection=database["user"]
collection.drop()

