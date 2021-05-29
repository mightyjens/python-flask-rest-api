import os, json

def helloworld():
    return "Hello World"

def isJson(inputJson):
    try:
        json_object = json.loads(inputJson)
    except ValueError as e:
        return False
    return True

def getValueFromEnv(key):
    try:
        result = os.environ[f"API_USER_{key.upper()}"]
        return result
    except:
        return None
