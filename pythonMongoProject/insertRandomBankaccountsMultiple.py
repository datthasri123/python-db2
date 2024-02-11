import random

from faker import Faker
from pymongo import MongoClient
import argparse
from datetime import datetime
import matplotlib.pyplot as plt
from pymongo.errors import BulkWriteError


def generate_random_15_digit_number():
    # Generate a random 15-digit number
    random_number = random.randint(10 ** 14, 10 ** 15 - 1)
    return str(random_number)


def generate_random_5_digit_number():
    # Generate a random 15-digit number
    random_number = random.randint(10000, 99999)
    return str(random_number)


def generate_random_10_digit_balance():
    # Generate a random 15-digit number
    random_number = random.uniform(10 ** 9, 10 ** 10 - 1)
    return random_number


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process key-value arguments.')

    start_datetime = datetime.now()

    # Add arguments
    parser.add_argument('--connection_string', type=str, help='first connection string')
    parser.add_argument('--database_name', type=str, help='second: database name')
    parser.add_argument('--collection_name', type=str, help='second: database name')
    parser.add_argument('--num_of_entries', type=int, help='second: database name')
    parser.add_argument('--batch_count', type=int, help='5: batch size')
    # Add more arguments as needed

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values using dot notation
    connection_string = args.connection_string
    database_name = args.database_name
    collection_name = args.collection_name
    num_of_entries = args.num_of_entries
    batch_count = args.batch_count

    # Connect to MongoDB
    client = MongoClient(connection_string)

    # Select the database
    db = client[database_name]

    # Select the collection
    collection_name = db[collection_name]

    fake = Faker()
    count = 0
    document_to_insert_list = []
    response_time_list = []

    # this is to fix number of entries we want to insert in to mongo
    while collection_name.count_documents({}) <= 89999:

        for _ in range(num_of_entries):

            count += 1
            db_insert_start_datetime = datetime.now()

            document_to_insert = {'country': random.choice(['IN', 'SA', 'EG']),
                                  'Institute': 'HBAP',
                                  'BankAccount': generate_random_5_digit_number(),
                                  'Account_type': 'CA',
                                  'Name': fake.name(),
                                  'CreditCard': fake.credit_card_number(),
                                  'CVV': fake.credit_card_security_code(),
                                  'PASSPORT_Number': fake.passport_number(),
                                  'ISDN': fake.phone_number(),
                                  'Balance': generate_random_10_digit_balance(),
                                  'Balance_date': start_datetime.date().isoformat(),
                                  'Insert_timestamp': start_datetime,
                                  'Update_timestamp': start_datetime
                                  }
            document_to_insert_list.append(document_to_insert)

            if count >= batch_count:
                count = 0
                try:
                    #ignore duplicates
                    result = collection_name.insert_many(document_to_insert_list, ordered=False)
                    db_insert_end_datetime = datetime.now()
                    time_difference = db_insert_end_datetime - db_insert_start_datetime
                    response_time_list.append(time_difference.microseconds)
                    print(
                        f"Number of docs inserted: {len(result.inserted_ids)}, inserted in microseconds: {time_difference.microseconds} microseconds")
                except BulkWriteError as bwe:
                    print("Number of docs inserted:", bwe.details['nInserted'] )
                document_to_insert_list = []

        if count > 0:
            count = 0
            try:
                # ignore duplicates
                result = collection_name.insert_many(document_to_insert_list, ordered=False)
                db_insert_end_datetime = datetime.now()
                time_difference = db_insert_end_datetime - db_insert_start_datetime
                response_time_list.append(time_difference.microseconds)
                print(
                    f"Number of docs inserted: {len(result.inserted_ids)}, inserted in microseconds: {time_difference.microseconds} microseconds")
            except BulkWriteError as bwe:
                print("Number of docs inserted:", bwe.details['nInserted'])
            document_to_insert_list = []

    end_datetime = datetime.now()

    # Calculate the time difference
    time_difference = end_datetime - start_datetime

    # Extract the total microseconds from the time difference
    seconds_difference = time_difference.seconds

    print(f"Process completed in: {seconds_difference} seconds")

    # Create a bar graph
    plt.bar(range(len(response_time_list)), response_time_list)

    # Add labels and title
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Bar Graph of List Values')

    # Show the graph
    plt.show()