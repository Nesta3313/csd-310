
#Richard Akindele
#Feb 1, 2022
#Module 5.2

#github repo

#https://github.com/Nesta3313/csd-310

import pymongo

from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.vzaco.mongodb.net/pytech?retryWrites=true&w=majority"

cluster = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)

# connect to pytech database
db = cluster.pytech

# show the connected collections
print("\n -- Pytech Collection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press any key to exit... ")