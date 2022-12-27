# https://stackskills.com/courses/102831/lectures/1499451

from pymongo import MongoClient
import datetime

# Create datetime instances in python
current_date= datetime.datetime.now()
old_date = datetime.datetime(2009, 8, 11)

# Access server
MyClient = MongoClient("mongodb://localhost:27017")
# Access or create database
DB = MyClient["my-database"]
# Access or create collection (drop if exists)
DB.drop_collection("users")
Users = DB["users"]


# Insert multiple documents
newUsers = [
    {
        "username": "user1",
        "password": "password",
        "favorite_number": 93,
        "hobbies": [
            "games",
            "programming",
            "reading"
        ],
        "date": current_date
    },
    {
        "username": "user2",
        "password": "password",
        "favorite_number": 93,
        "hobbies": [
            "games",
            "drawing"
        ],
        "date": old_date
    },
]

inserted = Users.insert_many(newUsers)
print("Inserted documents:", inserted.inserted_ids)


# Date is greater than or equal to value
print("\nDate is greater than", old_date)
for doc in Users.find({"date": {"$gt": old_date}}):
    print(doc)
# Date field exists
print("\nDate field exists")
for doc in Users.find({"date": {"$exists": True}}):
    print(doc)
# Not equal to
print("\nUsername not equal to user1")
for doc in Users.find({"username": {"$ne": "user1"}}):
    print(doc)
