from pymongo import MongoClient
from tqdm import tqdm
import os

dbname = ""
filePath = "../dehydrated/" + dbname + '/'

try:
    os.stat(filePath)
except:
    os.mkdir(filePath)

client = MongoClient("mongodb://ADDRESS:PORT/")
database = client[dbname]

dbsize = len(database.list_collection_names())

with tqdm(total=dbsize, position=0, leave=True) as pbar:
    for collectionname in database.list_collection_names():
        pbar.set_description("Processing " + collectionname)
        collection = database[collectionname]
        query = {}
        projection = {'status_id': 1, '_id': 0}
        cursor = collection.find(query, projection=projection)
        collectionSize = collection.count_documents(query)
        with tqdm(total=collectionSize, position=0, leave=True) as pbar2:
            with open(filePath + collectionname + '.dhy', 'a') as file:
                try:
                    for tweet in cursor:
                        file.write(tweet['status_id'] + '\n')
                        pbar2.update(1)
                finally:
                    client.close()
            pbar.update(1)
