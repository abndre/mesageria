#!/usr/bin/env python
from pymongo import MongoClient
from datetime import datetime
from nameko.rpc import rpc
from datetime import datetime
import time
from mongo_value import mongo_insert

class MongoSave:
    name = "dict"
    @rpc
    def save(self, message):
        time.sleep(10)
        mongo_insert(message)
        return "Update"
