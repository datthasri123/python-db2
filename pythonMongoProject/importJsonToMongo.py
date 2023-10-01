import json
import pymongo

myuri = 'mongodb://root:example@127.0.0.1:27017/admin?retryWrites=true&w=majority'
client = pymongo.MongoClient(myuri)
db = client.test
hotels_collection = db.hotels

# below will get the string output
with open(r'/home/siva/Downloads/archive(1)/file4.json', 'r') as f:
    line = f.read()

# convert to dictionary object
parsed_json = json.loads(line)

cnt = 0

for i in range(len(parsed_json)):

    # get the restaurants list from the dictionary, output will be dictionary
    restaurants = parsed_json[i]

    # check if there is restaurants keyword in keys, only that will have dictionaries
    if 'restaurants' in restaurants.keys():
        restaurants_list = restaurants['restaurants']
        if len(restaurants_list) > 0:
            hotels_collection.insert_many(restaurants_list)

exit(1)





