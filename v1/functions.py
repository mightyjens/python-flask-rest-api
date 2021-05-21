import os

def checkVersion():
    return os.path.basename(os.path.dirname(os.path.realpath(__file__)))

def checkRuntime():
    return os.environ.get('TEST_ENV_VAR')

def testRequest():
    import requests
    from requests.auth import HTTPBasicAuth

    response = requests.get('https://api.github.com/user', auth = HTTPBasicAuth('mightyjens', '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'))

    if response.status_code == 200:
        return response.json()
    else:
        return response.text
