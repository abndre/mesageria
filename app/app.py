from flask import Flask
from redis import Redis
import pika

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/pika')
def pikasend():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
    connection.close()

    return 'pika'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)