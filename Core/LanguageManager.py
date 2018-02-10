from googletrans import Translator
from Setting import DefineManager
from Utils import ResponseManager, LogManager

def OriginLanguageToTargetLanguage(text = '', dest = 'en'):
    translator = Translator()
    result = translator.translate(text, dest=dest)

    resultDic = {}
    resultDic["src"] = result.src
    resultDic["text"] = result.text
    resultDic["dest"] = result.dest

    LogManager.PrintLogMessage("LanguageManager", "OriginLanguageToTargetLanguage", "" + text + " -> " + resultDic["text"], DefineManager.LOG_LEVEL_INFO)
    return ResponseManager.TemplateOfResponse(DefineManager.SIMPLE_RESPONSE, resultDic["text"])
