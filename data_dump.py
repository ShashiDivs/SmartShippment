import pandas as pd
import pymongo
import json
from pymongo.mongo_client import MongoClient

client = "mongodb+srv://shashingit:divyashashi@divya.wtvvnub.mongodb.net/?retryWrites=true&w=majority"
DATA_FILE_PATH = (r"C:\Users\Admin\Desktop\train.csv")
DATABASE = "Machine_Learning"
COLLECTION_NAME = "DATASET"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE][COLLECTION_NAME].insert_many(json_record)
    