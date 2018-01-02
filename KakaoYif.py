from flask import Flask
import json
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/keyboard', methods=['GET'])
def test_keyboard():

    testResponse = {}
    testResponse["type"] = "buttons"
    testResponse["buttons"] = ["select 1", "select 2", "select 3"]

    jsonResponse = json.dumps(testResponse)
    return jsonResponse

@app.route('/message', methods=['POST'])
def test_message():
    requestJsonData = request.get_json(silent=True)

    requestStr = "user key: " + requestJsonData["user_key"] + " content: " + requestJsonData["content"] + " type: " + requestJsonData["type"]

    testResponse = {}

    testMessage = {}

    testPhoto = {}
    testPhoto["url"] = "http://211.249.49.198/profile.png"
    testPhoto["width"] = "512"
    testPhoto["height"] = "515"

    testMessageButton = {}
    testMessageButton["label"] = "Label button"
    testMessageButton["url"] = "http://211.249.49.198"

    testMessage["text"] = requestStr
    testMessage["photo"] = testPhoto
    # testMessage["message_button"] = testMessageButton

    testKeyboardResponse = {}
    testKeyboardResponse["type"] = "buttons"
    testKeyboardResponse["buttons"] = ["select 1", "select 2", "select 3"]

    testResponse["message"] = testMessage
    testResponse["keyboard"] = testKeyboardResponse

    jsonResponse = json.dumps(testResponse)


    response = app.response_class(
        response=jsonResponse,
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6100, threaded=True)
