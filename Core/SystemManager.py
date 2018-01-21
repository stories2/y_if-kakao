from Utils import ResponseManager, LogManager
from Setting import DefineManager

def CheckVersion():
    version = DefineManager.VERSION
    LogManager.PrintLogMessage("SystemManager", "CheckVersion", "this version is " + version, DefineManager.LOG_LEVEL_INFO)
    return ResponseManager.TemplateOfResponse(DefineManager.SIMPLE_RESPONSE, version)

def Echo(text):
    LogManager.PrintLogMessage("SystemManager", "Echo", "echo text: " + text, DefineManager.LOG_LEVEL_INFO)
    return ResponseManager.TemplateOfResponse(DefineManager.SIMPLE_RESPONSE, text)