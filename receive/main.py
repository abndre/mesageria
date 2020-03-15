#!/usr/bin/env python
import pika
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

	return colection.insert_one(payload).inserted_id

def callback(ch, method, properties, body):
    mongo_insert("nada")
    print(" [x] Received %r" % body)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq1'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()