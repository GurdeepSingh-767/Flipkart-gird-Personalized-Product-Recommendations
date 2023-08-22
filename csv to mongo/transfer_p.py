import csv
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['flipkart']
collection = database['main_app_product']

with open(r'C:\Users\lenovo\Downloads\flipkart\frontend_myshop\csv to mongo\product_detail1.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        collection.insert_one(row)

print("CSV data inserted into MongoDB collection.")
