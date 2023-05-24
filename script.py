import pymongo
import pandas as pd

conect = pymongo.MongoClient("mongodb://localhost:27017/")
db = conect["mongodb1"]
coll = db["col1"]

datos = pd.read_csv("atp_tennis.csv").to_dict(orient="records")

if coll.count_documents({}) == 0:    
    coll.insert_many(datos)
else:    
    docs = coll.find()
    for x in docs:
        print(x)

conect.close()