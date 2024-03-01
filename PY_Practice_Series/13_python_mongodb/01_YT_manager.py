import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://atokvedjanak:mongodbjanak@cluster0.bzbtf1i.mongodb.net")
db = client["ytmanager"]

vedio_collection = db["videos"]
