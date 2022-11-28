import random
import pika
from faker import Faker

def send_message():

    credentials = pika.PlainCredentials('myuser', 'mypassword')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port='5672', credentials=credentials))
    channel = connection.channel()

    fake = Faker()

    message = fake.name() + 'has ' + random.choice(['CREDITED', 'DEBITED']) + ' amount from Bank'
    channel.basic_publish(exchange='test', routing_key='C', body=message)


channel.close()