from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/get_random_word', methods=['GET'])
def get_random_word():
    words = ['nikyl', 'sandy', 'madhu', 'fida', 'mano', 'sacky', 'narasingan', 'Krishna', 'lathish']
    random_word = random.choice(words)
    return jsonify({'word': random_word})

