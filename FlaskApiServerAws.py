from flask import Flask, request, jsonify, escape
from ClientMongoDB import MongoDBClient
from bson.json_util import dumps
import requests
import json

app = Flask(__name__)


@app.route('/id/<int:tweet_id>', methods=['GET'])
def post_request(tweet_id):
    try:
        response = MongoDBClient().read_db({"id": str(tweet_id)})
        if response is None:
            resp = requests.get(
                "https://bef5-34-122-234-12.ngrok.io/?id={}&fbclid=IwAR35Wdjb4RAEPSBOYHfikQQ9JcgkYtUjan9W3OA_N-OC0nEChclQ648PGQ0".format(
                    tweet_id))

            response = {"id": str(tweet_id), "model_output": resp.json()["prob"]}
            MongoDBClient().update_db(response)
            return json.loads(dumps({str(tweet_id): resp.json()["prob"]}))

        else:
            return jsonify({response["id"]: response["model_output"]})

    except TypeError:
        return "RATE LIMITS", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
