from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
cors = CORS(app)


@app.route('/get_random_word', methods=['GET'])
def get_random_word():
    words = ['nikyl', 'sandy', 'madhu', 'fida', 'mano', 'sacky', 'narasingan', 'Krishna', 'lathish']
    random_word = random.choice(words)
    return jsonify({'word': random_word})

