import v1.functions
import common.functions

from flask import Blueprint

api = Blueprint('api_v1', __name__)

@api.route('/')
def index():
    return f"{v1.functions.checkVersion()} on {v1.functions.checkRuntime()}"

@api.route('/test')
def test():
    return v1.functions.testRequest()

    