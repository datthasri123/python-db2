import random

import requests
from faker import Faker

fake = Faker()

i = 5679

for i in range(100000):
    i += 1
    api_url = "http://localhost:8080/home/insert"
    json_inp = {"studentId": i, "name": fake.name(), "age": random.choice([31, 32, 33])}
    response = requests.post(api_url, json=json_inp)
    print(response)
