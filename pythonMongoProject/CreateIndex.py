import pymongo
from pymongo import MongoClient
import argparse
from datetime import datetime


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process key-value arguments.')

    start_datetime = datetime.now()

    # Add arguments
    parser.add_argument('--connection_string', type=str, help='first connection string')
    parser.add_argument('--database_name', type=str, help='second: database name')
    parser.add_argument('--collection_name', type=str, help='third: collection name')
    parser.add_argument('--index_key', type=str, help='fourth: index key')
    parser.add_argument('--index_Name', type=str, help='5: index Name')
    # Add more arguments as needed

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values using dot notation
    connection_string = args.connection_string
    database_name = args.database_name
    collection_name = args.collection_name
    indx_key = args.index_key
    index_name = args.index_Name

    # Connect to MongoDB
    client = MongoClient(connection_string)

    # Select the database
    db = client[database_name]

    # Select the collection
    collection_name = db[collection_name]

    list_of_indexes = indx_key.split()
    index_key = []

    # Use pymongo.ASCENDING for ascending index
    for key in list_of_indexes:
        # Use pymongo.ASCENDING for ascending index
        index_key.append((key, pymongo.ASCENDING))

    print(index_key)
    index_creation_op = collection_name.create_index(index_key, name=index_name, unique=True)
    print(index_creation_op)

    print("Index created successfully.")
