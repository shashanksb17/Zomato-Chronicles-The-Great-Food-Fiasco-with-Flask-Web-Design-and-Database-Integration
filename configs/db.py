from pymongo import MongoClient

# Configure the MongoDB connection
client = MongoClient('mongodb+srv://shashank:shaila@cluster0.la0uy.mongodb.net/zestyZomato?retryWrites=true&w=majority')
db = client['zesty_zomato']  # Create or use an existing database
