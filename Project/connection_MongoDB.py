from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("mongodb://db102stock:db102stock_pwd@10.120.14.28:27017/stock")
db = conn.stock
collection = db.stocklisted


cursor = collection.find({})
data = [d for d in cursor]
print(data)
