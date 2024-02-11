import random

from faker import Faker
from pymongo import MongoClient
import argparse
from datetime import datetime


def generate_random_15_digit_number():
    # Generate a random 15-digit number
    random_number = random.randint(10**14, 10**15 - 1)
    return str(random_number)


def generate_random_10_digit_balance():
    # Generate a random 15-digit number
    random_number = random.uniform(10**9, 10**10 - 1)
    return random_number


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process key-value arguments.')

    start_datetime = datetime.now()

    # Add arguments
    parser.add_argument('--connection_string', type=str, help='first connection string')
    parser.add_argument('--database_name', type=str, help='second: database name')
    parser.add_argument('--collection_name', type=str, help='second: database name')
    parser.add_argument('--num_of_entries', type=int, help='second: database name')
    # Add more arguments as needed

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values using dot notation
    connection_string = args.connection_string
    database_name = args.database_name
    collection_name = args.collection_name
    num_of_entries = args.num_of_entries

    # Connect to MongoDB
    client = MongoClient(connection_string)

    # Select the database
    db = client[database_name]

    # Select the collection
    collection_name = db[collection_name]

    fake = Faker()

    for _ in range(num_of_entries):

        db_insert_start_datetime = datetime.now()

        document_to_insert = {'country': random.choice(['IN', 'SA', 'EG']),
                              'Institute': 'HBAP',
                              'BankAccount': generate_random_15_digit_number(),
                              'Account_type': 'CA',
                              'Name': fake.name(),
                              'CreditCard': fake.credit_card_number(),
                              'CVV': fake.credit_card_security_code(),
                              'PASSPORT Number': fake.passport_number(),
                              'ISDN': fake.phone_number(),
                              'Balance': generate_random_10_digit_balance(),
                              'Balance_date': start_datetime.date().isoformat(),
                              'Insert_timestamp': start_datetime,
                              'Update_timestamp': start_datetime
                              }
        result = collection_name.insert_one(document_to_insert)
        db_insert_end_datetime = datetime.now()
        time_difference = db_insert_end_datetime - db_insert_start_datetime
        print(f"Document inserted with ID: {result.inserted_id}, inserted in microseconds: {time_difference.microseconds} microseconds")

    end_datetime = datetime.now()

    # Calculate the time difference
    time_difference = end_datetime - start_datetime

    # Extract the total microseconds from the time difference
    seconds_difference = time_difference.seconds

    print(f"Process completed in: {seconds_difference} second")