import json
import pymongo

myuri = 'mongodb://root:example@127.0.0.1:27017/admin?retryWrites=true&w=majority'
client = pymongo.MongoClient(myuri)
db = client.test
swiggy_collection = db.swiggy

# below will get the string output
with open(r'/home/siva/Downloads/async-demo-main/data.json', 'r') as f:
    line = f.read()

# convert to dictionary object
parsed_json = json.loads(line)
parsed_json_list = []
for i in parsed_json.keys():
    region = i
    if 'restaurants' in parsed_json[i]:
        region_restaurants = parsed_json[i]['restaurants']
        for restaurant_id in parsed_json[i]['restaurants'].keys():
            restaurant_doc = parsed_json[i]['restaurants'][restaurant_id]
            restaurant_doc['rid'] = restaurant_id
            restaurant_doc['region'] = i
            parsed_json_list.append(restaurant_doc)

        if len(parsed_json_list) > 0:
            swiggy_collection.insert_many(parsed_json_list)
            parsed_json_list = []

# print(parsed_json.keys())
# print(parsed_json['Satna']['restaurants'])
# print(parsed_json['Satna']['restaurants'].keys())
# print(type(parsed_json))
# print((parsed_json[0]))
# cnt = 0