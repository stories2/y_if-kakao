from Core import SystemManager
from Setting import DefineManager
from Utils import LogManager

def MessageReceived(userName, channelName, channelId, text):
    LogManager.PrintLogMessage("SlackManager", "MessageReceived", "userName: " + userName + " channelName: " + channelName +
                               " channelId: " + channelId + " text: " + text, DefineManager.LOG_LEVEL_INFO)
    text = "userName: " + userName + " channelName: " + channelName + " channelId: " + channelId + " text: " + text

    coreResponse = SystemManager.Echo(text)
    testResponse = {}
    if coreResponse["type"] == DefineManager.SIMPLE_RESPONSE:
        testResponse["pretext"] = coreResponse["data"]
    # elif coreResponse["type"] == DefineManager.URL_ADDED_RESPONSE:

    return testResponse