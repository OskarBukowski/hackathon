from flask import Flask, request, jsonify, escape

from ClientMongoDB import MongoDBClient
from waitress import serve




app = Flask(__name__)


# {"id": 12345678, "model_output": 1.0}

@app.route('/id/<int:tweet_id>', methods=['GET'])
def post_request(tweet_id):
    # if exist in database
    response = MongoDBClient().read_db({"id": tweet_id})
    if response is None:
        # there we execute the AI class
        print("Executing class")

    else:
        return jsonify({response['id']: response['model_output']})




if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)