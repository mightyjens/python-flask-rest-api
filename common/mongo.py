import os
from pymongo import MongoClient

def getUserFromDatabase(username):

    cosmos_user_name = os.environ["COSMOS_ACCOUNT_USER"]
    cosmos_password = os.environ["COSMOS_ACCOUNT_KEY"]
    cosmos_url = os.environ["COSMOS_ACCOUNT_HOST"]
    cosmos_database_name = os.environ["COSMOS_DATABASE_NAME"]
    cosmos_collection_name = os.environ["COSMOS_COLLECTION_NAME"]

    # Create Mongo client
    mongoUri = f'mongodb://{cosmos_user_name}:{cosmos_password}@{cosmos_url}'
    mongoClient = MongoClient(mongoUri)
    
    # This is the name of the Mongo compatible database
    mongoDatabase = mongoClient[cosmos_database_name]
    
    # The name of the collection you are querying
    mongoCollection = mongoDatabase[cosmos_collection_name]
    mongoDocument = mongoCollection.find_one({ "username": username})
    
    # Get password from the collection
    
    if mongoDocument:
        return mongoDocument['password']
    else: 
        return None