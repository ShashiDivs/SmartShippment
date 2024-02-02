import pandas as pd
import pymongo
import json
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://shashingit:divyashashi@cluster0.g3ja9af.mongodb.net/?retryWrites=true&w=majority"
DATA_FILE_PATH = (r"C:\Users\Admin\Desktop\train.csv")
DATABASE = "Machine_Learning"
COLLECTION_NAME = "DATASET"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns : {df.shape}")

    #convert the DataFrame to a list of dictionaries (json records)
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])

    #Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)

    #Access the desired database and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

    #Insert the JSON records into the collection
    collection.insert_many(json_records)

    #close the MongoDB connection
    client.close()
    