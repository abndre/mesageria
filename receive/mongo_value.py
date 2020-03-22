from pymongo import MongoClient

import datetime

# MONGO
def mongo_insert(message):
	cliente = MongoClient('mongo', 27017)

	banco = cliente.test

	colection = banco.values

	payload = {
		"data": datetime.datetime.now(),
		"message": message
		}

	return colection.insert_one(payload)

if __name__ == "__main__":
	mongo_insert("Local")
