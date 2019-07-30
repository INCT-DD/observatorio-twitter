from pymongo import MongoClient
from tqdm import tqdm

dbname = ""
collectionname = ""
fileName = "../dehydrated/" + collectionname + ".dhy"

client = MongoClient("mongodb://ADDRESS:PORT/")
database = client[dbname]
collection = database[collectionname]

query = {}
projection = {'status_id': 1, '_id': 0}

collectionSize = collection.count_documents(query)

cursor = collection.find(query, projection=projection)
with tqdm(total=collectionSize, position=0, leave=True) as pbar:
    with open(fileName, 'a') as file:
        try:
            for tweet in cursor:
                file.write(tweet['status_id'] + '\n')
                pbar.update(1)
        finally:
            client.close()
