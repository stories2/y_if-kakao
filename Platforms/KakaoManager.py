from Setting import DefineManager
from Utils import LogManager
from Core import SystemManager

def InitKeyboard():
    LogManager.PrintLogMessage("KakaoManager", "InitKeyboard", "init user keyboard", DefineManager.LOG_LEVEL_INFO)
    testResponse = {}
    testResponse["type"] = "buttons"
    testResponse["buttons"] = ["select 1", "select 2", "select 3"]
    return testResponse

def MessageReceived(userKey, content, type):
    LogManager.PrintLogMessage("KakaoManager", "MessageReceived", "userKey: " + userKey + " content: " + content + " type: " + type, DefineManager.LOG_LEVEL_INFO)
    text = "userKey: " + userKey + " content: " + content + " type: " + type
    coreResponse = SystemManager.Echo(text)

    testResponse = {}
    testMessage = {}

    if coreResponse["type"] == DefineManager.SIMPLE_RESPONSE:
        testMessage["text"] = coreResponse["data"]
    # elif coreResponse["type"] == DefineManager.URL_ADDED_RESPONSE:

    # testMessageButton = {}
    # testMessageButton["label"] = "Label button"
    # testMessageButton["url"] = "http://211.249.49.198"

    testKeyboardResponse = {}
    testKeyboardResponse["type"] = "buttons"
    testKeyboardResponse["buttons"] = ["select 1", "select 2", "select 3"]

    testResponse["message"] = testMessage
    testResponse["keyboard"] = testKeyboardResponse
    return testResponse

def HelloNewFriend(userKey):
    LogManager.PrintLogMessage("KakaoManager", "HelloNewFriend", "hello userKey: " + userKey, DefineManager.LOG_LEVEL_INFO)
    testResponse = {}

    testMessage = {}
    testMessage["text"] = "Hello, " + userKey

    testResponse["message"] = testMessage
    return testResponse

def DeleteFriend(userKey):
    testResponse = {}

    testMessage = {}
    if userKey != None:
        testMessage["text"] = "Bye, " + userKey
        LogManager.PrintLogMessage("KakaoManager", "DeleteFriend", "bye, userKey: " + userKey, DefineManager.LOG_LEVEL_INFO)
    else:
        testMessage["text"] = "Bye, anonymous"
        LogManager.PrintLogMessage("KakaoManager", "DeleteFriend", "bye, anonymous", DefineManager.LOG_LEVEL_WARN)

    testResponse["message"] = testMessage
    return testResponse

def LeftFromChatRoom(userKey):
    testResponse = {}

    testMessage = {}
    if userKey != None:
        testMessage["text"] = "See ya, " + userKey
        LogManager.PrintLogMessage("KakaoManager", "LeftFromChatRoom", "see ya, userKey: " + userKey, DefineManager.LOG_LEVEL_INFO)
    else:
        testMessage["text"] = "See ya, anonymous"
        LogManager.PrintLogMessage("KakaoManager", "LeftFromChatRoom", "see ya, anonymous", DefineManager.LOG_LEVEL_WARN)

    testResponse["message"] = testMessage
    return testResponse