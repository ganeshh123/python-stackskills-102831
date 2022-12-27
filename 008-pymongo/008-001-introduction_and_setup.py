# https://stackskills.com/courses/102831/lectures/1499446

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.pytests