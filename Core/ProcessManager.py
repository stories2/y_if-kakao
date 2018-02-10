from Utils import LogManager, ResponseManager
from Setting import DefineManager
from Core import LanguageManager, SystemManager
import re

def ExecuteOrder(orderDic):
    orderArgs = []
    orderArgs = orderDic["text"].split("  ")
    orderArgs[DefineManager.ORDER_SAVED_POINT] = re.sub("[?|<|>|?|:|/|!]", "", orderArgs[DefineManager.ORDER_SAVED_POINT]) #orderArgs[DefineManager.ORDER_SAVED_POINT].replace("!", "")
    LogManager.PrintLogMessage("ProcessManager", "ExecuteOrder", "execute order args: " + " | ".join(orderArgs), DefineManager.LOG_LEVEL_INFO)
    if orderArgs[DefineManager.ORDER_SAVED_POINT] == "translate":
        return LanguageManager.OriginLanguageToTargetLanguage(orderArgs[2], orderArgs[1])
    elif orderArgs[DefineManager.ORDER_SAVED_POINT] == "echo":
        return SystemManager.Echo(orderArgs[1])
    else:
        return ResponseManager.TemplateOfResponse(DefineManager.SIMPLE_RESPONSE, orderArgs[DefineManager.ORDER_SAVED_POINT])
