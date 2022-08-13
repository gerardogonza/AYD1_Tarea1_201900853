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

@app.route('/info', methods=['GET'])
def info():
    return jsonify({'Carne': 201900853,'Nombre':'Gerardo Steve Munoz Contreras'})

@app.route('/resta/<int:num1>-<int:num2>', methods=['POST'])
def resta(num1,num2):
    return jsonify({'result': num1-num2})

@app.route('/multi/<int:num1>*<int:num2>', methods=['POST'])
def multi(num1,num2):
    return jsonify({'result': num1*num2})

if __name__ == '__main__':
    app.run(debug=True,port=3000)
    