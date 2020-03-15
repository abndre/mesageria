import pika
from pymongo import MongoClient

import datetime

# MONGO
def mongo_insert(message):
	cliente = MongoClient('localhost', 27017)

	banco = cliente.test

	colection = banco.values

	payload = {
		"data": datetime.datetime.now(),
		"message": message
		}

	return colection.insert_one(payload).inserted_id

if __name__ == "__main__":
	mongo_insert()
