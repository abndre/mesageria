from flask import Flask, request
from nameko.standalone.rpc import ClusterRpcProxy
AMQP_URI = 'pyamqp://guest:guest@rabbitmq1'

app = Flask(__name__)

CONFIG = {
    'AMQP_URI': AMQP_URI
}


@app.route('/mongo', methods=['POST'])
def compute():
    if request.method == 'POST':
        message = request.json.get('message')
        msg = "Please wait the calculation, you'll receive an email with results"
        with ClusterRpcProxy(CONFIG) as rpc:
            rpc.dict.save(message)
            return msg, 200
    elif request.method == 'GET':
        return 'not exist', 201


if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=5000)