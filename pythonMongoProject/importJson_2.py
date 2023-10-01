import json

# below will get the string output
with open(r'/home/siva/Downloads/async-demo-main/data.json', 'r') as f:
    line = f.read()

# convert to dictionary object
parsed_json = json.loads(line)
print(type(parsed_json))
# print((parsed_json[0]))

cnt = 0
#
# for i in range(len(parsed_json)):
#     # print(type(parsed_json[i]))
#     restaurants = parsed_json[i]
#     # print(restaurants.keys())
#     if 'restaurants' in restaurants.keys():
#         restaurants_list = restaurants['restaurants']
#         # print(json.dumps(restaurants_list, indent=2))
#         cnt += len(restaurants_list)
#
# print(cnt)
# # print(type(restaurants_list))
# # print(len(restaurants_list))
# exit(1)


# print(len(parsed_json))
# print(type(parsed_json[0]))
# json_data = json.dumps(parsed_json[0], indent=2)
# print(json_data)
# print(parsed_json[0])




