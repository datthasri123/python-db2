import pymongo

with open(r'/home/siva/Downloads/mongodb-json-files-master/datasets/people.bson', 'rb') as f:
    data = pymongo.bson.decode_all(f.read())
    print(type(data))
