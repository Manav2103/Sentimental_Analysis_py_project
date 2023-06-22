from pymongo import MongoClient

client = MongoClient('mongodb+srv://yashdave307:yashdave307@cluster0.qd3g00c.mongodb.net/test');
print("Connection Successful")
print(client)

db = client['sentimental_analysis']
collection = db['users']

client.close();

