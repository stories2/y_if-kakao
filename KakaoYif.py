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
    userName = request.form.get('user_name')
    channelName = request.form.get('channel_name')
    channelId = request.form.get('channel_id')
    text = request.form.get('text')

    order = request.args.get('order')
    token = request.args.get('token')

    if order != None:
        text = order + DefineManager.ORDER_SEPERATE_CHARACTER + DefineManager.ORDER_SEPERATE_CHARACTER + text

    testResponse = SlackManager.MessageReceived(userName, channelName, channelId, text)

    if token != None:
        slack = Slacker(token)
    slack = Slacker(DefineManager.SLACK_TOKEN)
    slack.chat.post_message('#' + channelName, text = None, attachments = [testResponse])
    return Response(), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
