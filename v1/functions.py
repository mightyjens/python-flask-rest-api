import os

def checkVersion():
    return os.path.basename(os.path.dirname(os.path.realpath(__file__)))

def checkRuntime():
    return os.environ.get('TEST_ENV_VAR')
