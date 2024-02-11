from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser(description='Process key-value arguments.')

# Add arguments
parser.add_argument('--connection_string', type=str, help='first connection string')
parser.add_argument('--database_name', type=str, help='second: database name')
# Add more arguments as needed

# Parse the command-line arguments
args = parser.parse_args()

# Access the values using dot notation
connection_string = args.connection_string
database_name = args.database_name

# Connect to MongoDB
client = MongoClient(connection_string)

# Select the database
db = client[database_name]

# Drop the database
client.drop_database(database_name)
