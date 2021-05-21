import os
from flask import Response
from azure.cosmos import exceptions, CosmosClient, PartitionKey

def getUserFromDatabase():

    # [START create_client]
    url = os.environ["COSMOS_ACCOUNT_URI"]
    key = os.environ["COSMOS_ACCOUNT_KEY"]
    db = os.environ["COSMOS_DATABASE_NAME"]
    con = os.environ["COSMOS_CONTAINER_NAME"]
    
    client = CosmosClient(url, key)
    # [END create_client]
    


    database = client.create_database(id=db)


    # try:
    #     # query for a database
    #     database = readDatabase(client, db)
    # except exceptions.CosmosHttpResponseError as e:
    #     return Response('Cosmos db has caught an error. {0}'.format(e.message), status=500)


    # database.create_container(
    #     id='apiuser',
    #     partition_key=PartitionKey(path="/apiuser"),
    #     default_ttl=200)

#    for container in database.list_containers():
#        print("Container ID: {}".format(container['id']))
    
    
    # try:
    #     # query for a container
    #     container = getContainer(database, con)
    # except exceptions.CosmosHttpResponseError as e:
    #     return Response('Cosmos db has caught an error. {0}'.format(e.message), status=500)

    
    # database_name = os.environ["COSMOS_DATABASE_NAME"]
    # database = client.get_database_client(database=database_name)


    # container_name =  os.environ["COSMOS_CONTAINER_NAME"]
    # container = database.get_container_client(container_name)

    return "User"


def readDatabase(client, id):
    print("1. Get Database")

    try:
        database = client.get_database_client(id)
        print('Database with id \'{0}\' was found, it\'s link is {1}'.format(id, database.database_link))
        return database
    except exceptions.CosmosResourceNotFoundError:
        print('A database with id \'{0}\' does not exist'.format(id))


def getContainer(db, id):
    print("2. Get Container")

    try:
        # read the container, so we can get its _self
        container = db.get_container_client(container=id)

        # now use its _self to query for Offers
        offer = container.read_offer()

        print('Found Offer \'{0}\' for Container \'{1}\' and its throughput is \'{2}\''.format(offer.properties['id'], container.id, offer.properties['content']['offerThroughput']))

        return container
    except exceptions.CosmosResourceExistsError:
        print('A container with id \'{0}\' does not exist'.format(id))



def list_Containers(db):
    print("5. List all Container in a Database")

    print('Containers:')

    containers = list(db.list_containers())

    if not containers:
        return

    for container in containers:
        print(container['id'])
