#!/usr/bin/env python
from pymongo import MongoClient
from datetime import datetime
from nameko.rpc import rpc
from datetime import datetime

save_dict ={}
# MONGO
def mongo_insert(message=""):
	cliente = MongoClient('mongo', 27017)

	banco = cliente.test

	colection = banco.values

	payload = {
		"data": datetime.now(),
		"message": message
		}

	return colection.insert_one(payload).inserted_id


class MongoSave:
    name = "dict"
    global save_dict
    @rpc
    def save(self, message):
        mongo_insert(message)
        return "Update"
