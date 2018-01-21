from flask import Flask
import json
from flask import request, Response
from slacker import Slacker
from Setting import DefineManager
from Platforms import KakaoManager, SlackManager

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/keyboard', methods=['GET'])
def test_keyboard():

    testResponse = KakaoManager.InitKeyboard()

    jsonResponse = json.dumps(testResponse)
    return jsonResponse

@app.route('/message', methods=['POST'])
def test_message():
    requestJsonData = request.get_json(silent=True)

    testResponse = KakaoManager.MessageReceived(requestJsonData["user_key"] or "", requestJsonData["content"] or "", requestJsonData["type"] or "")

    jsonResponse = json.dumps(testResponse)

    response = app.response_class(
        response=jsonResponse,
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/friend', methods=['POST'])
def test_friend():
    requestJsonData = request.get_json(silent=True)

    testResponse = KakaoManager.HelloNewFriend(requestJsonData["user_key"] or "")

    jsonResponse = json.dumps(testResponse)

    response = app.response_class(
        response=jsonResponse,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/friend/<user_key>', methods=['DELETE'])
def test_bye(user_key = None):
    testResponse = KakaoManager.DeleteFriend(user_key or "")

    jsonResponse = json.dumps(testResponse)

    response = app.response_class(
        response=jsonResponse,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/chat_room/<user_key>', methods=['DELETE'])
def test_seeya(user_key = None):
    testResponse = KakaoManager.LeftFromChatRoom(user_key or "")

    jsonResponse = json.dumps(testResponse)

    response = app.response_class(
        response=jsonResponse,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/slack/message', methods=['POST'])
def test_slack():
    requestJsonData = request.get_json(silent = True)
    userName = requestJsonData['user_name']
    channelName = requestJsonData['channel_name']
    channelId = requestJsonData['channel_id']
    text = requestJsonData['text']

    testResponse = SlackManager.MessageReceived(userName, channelName, channelId, text)

    slack = Slacker(DefineManager.SLACK_TOKEN)
    slack.chat.post_message('#' + channelName, text = None, attachments = [testResponse])
    return Response(), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
