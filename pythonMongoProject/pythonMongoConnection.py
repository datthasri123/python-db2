import pymongo


def insert_into_mongodb_posts_collection(obj):
    posts = db.posts
    # post_id = posts.insert_one(obj).inserted_id
    posts.insert_one(obj)
    # print(post_id)


myuri = 'mongodb://root:example@127.0.0.1:27017/admin?retryWrites=true&w=majority'
client = pymongo.MongoClient(myuri)
db = client.test
post = {
    "name": "ABC",
    "text": "first mongo python program"
}

insert_into_mongodb_posts_collection(post)
post['name'] = 'DEF'
del post['_id']
insert_into_mongodb_posts_collection(post)


# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print(post_id)