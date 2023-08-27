from pymongo import MongoClient

# Connect to server
client = MongoClient(host=<"hostName">, port=<portNum>)

# Connect to database
db = client[<"databaseName">]

# Get collection
dar = db[<"collectionName">]
