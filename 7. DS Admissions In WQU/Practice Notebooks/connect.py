""" Connecting to the Database """

import imports


# Connect to database
# Access a certain collection

# Create a Mongo-`client`
client = MongoClient(host="localhost", port=<portNumber>)

# Create a database: `db`
db = client["wqu-abtest"]

# Find your collection: `"<collectionName>"`
mscfe_app = db["<collectionName>"]
