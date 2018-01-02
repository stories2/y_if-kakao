from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/keyboard')
def test_keyboard():

    testResponse = {}
    testResponse["type"] = "buttons"
    testResponse["buttons"] = ["select 1", "select 2", "select 3"]

    jsonResponse = json.dumps(testResponse)
    return jsonResponse

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6100, threaded=True)
