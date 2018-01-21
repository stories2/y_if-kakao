from Setting import DefineManager

def TemplateOfResponse(type, data):
    response = {}
    response["type"] = type
    response["data"] = data
    return response