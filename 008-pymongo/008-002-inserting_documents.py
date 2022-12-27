# https://stackskills.com/courses/102831/lectures/1499447

from pymongo import MongoClient

# Access server
myClient = MongoClient("mongodb://localhost:27017")
# Access or create database
db = myClient["my-database"]
# Access or create collection
users = db["users"]

# Create a new document
user1 = {
    "username": "ganesh",
    "password": "password",
    "favorite_number": 93,
    "hobbies": [
        "games",
        "programming",
        "reading"
    ]
}
user_id = users.insert_one(user1)
print(user_id)
