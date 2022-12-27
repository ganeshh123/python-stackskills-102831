# https://stackskills.com/courses/102831/lectures/1499450

from pymongo import MongoClient

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
        ]
    },
    {
        "username": "user2",
        "password": "password",
        "favorite_number": 93,
        "hobbies": [
            "games",
            "drawing"
        ]
    },
    {
        "username": "user3",
        "password": "password",
        "favorite_number": 575,
        "hobbies": []
    }
]
Users.insert_many(newUsers)

# Count documents with filters
print(Users.count_documents({
    "favorite_number": 93,
    "hobbies": {"$all": ["games","programming","reading"]}
}))
