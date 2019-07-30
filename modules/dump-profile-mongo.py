from bson import json_util
import twint
import contextlib
import pymongo
import sys

mongoUser = ""
mongoPasswd = ""
mongoHost = ""
mongoPort = ""

searchParameters = twint.Config()

# referTo: https://github.com/twintproject/twint/wiki/Module

searchParameters.Username = ""
searchParameters.Output = ""
searchParameters.Stats = True
searchParameters.Store_json = True
searchParameters.Profile_full = True
searchLog = ""

print("Running search...")

with open(searchLog, 'a') as f:
    with contextlib.redirect_stdout(f):
        twint.run.Search(searchParameters)

print("Search finished.")

mongoUrl = ''.join(["mongodb://", mongoUser, ":", mongoPasswd, "@", mongoHost, ":", mongoPort])

try:
    mongoConnection = pymongo.MongoClient(mongoUrl)
    insertDatabase = mongoConnection[searchParameters.Username]
    insertCollection = insertDatabase['tweets']
except:
    print("CONNECTION ERROR. PLEASE CHECK YOUR DATABASE URL")
    sys.exit(1)

print("Loading data file to memory...")

with open(searchParameters.Output, 'r') as dataFile:
    dataStream = [json_util.loads(line) for line in dataFile]

print("Loading finished.")

print("Persisting tweets to the database...")

for tweet in dataStream:
    insertCollection.insert(tweet)

print("OK.")
