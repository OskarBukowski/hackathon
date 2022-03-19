from flask import Flask, request, jsonify, escape
from ClientMongoDB import MongoDBClient
from flask_sslify import SSLify
import requests
import json

app = Flask(__name__)


# {"id": 12345678, "model_output": 1.0}

@app.route('/id/<int:tweet_id>', methods=['GET'])
def post_request(tweet_id):
    # if exist in database
    response = MongoDBClient().read_db({"id": tweet_id})
    if response is None:
        resp = request.get(f"https://fdd3-34-136-46-201.ngrok.io/?id={tweet_id}&fbclid=IwAR0OGQZ25H5zaBptAhLh7nIKBqWSD5cAnhp4p6BUPYBQK9D-ZMD1N-Shezs")
        prob = resp.json()['prob']
        response = {"id": tweet_id, "model_output": prob}
        MongoDBClient().update_db(response)
        return jsonify(response)

    else:
        return jsonify({response['id']: response['model_output']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
