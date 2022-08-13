from json import JSONDecoder, JSONEncoder
import json
from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/info', methods=['GET'])
def info():
    return jsonify({'Carne': 201900853,'Nombre':'Gerardo Steve Munoz Contreras'})

if __name__ == '__main__':
    app.run(debug=True,port=4000)
    