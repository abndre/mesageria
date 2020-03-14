import pika
from pymongo import MongoClient

import datetime

# MONGO
def mongo_insert():
	cliente = MongoClient('localhost', 27017)

	banco = cliente.test

	colection = banco.values

	payload = {
		"data": datetime.datetime.now()
		}

	return colection.insert_one(payload).inserted_id

#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#channel = connection.channel()

if __name__ == "__main__":
	mongo_insert()
