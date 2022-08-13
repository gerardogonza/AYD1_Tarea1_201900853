from json import JSONDecoder, JSONEncoder
import json
from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/calc/<int:num1>+<int:num2>', methods=['POST'])
def calc(num1, num2):
    return jsonify({'result': num1 + num2})

if __name__ == '__main__':
    app.run(debug=True,port=3000)
    