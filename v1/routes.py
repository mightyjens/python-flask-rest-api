from v1.functions import checkRuntime, checkVersion, testRequest
from common.authy import auth
from flask import Blueprint

import common.cosmos


api = Blueprint('api_v1', __name__)

@api.route('/')
def index():
    return f"{checkVersion()} on {checkRuntime()}"

@api.route('/test')
@auth.login_required
def test():
    return common.cosmos.getUserFromDatabase()
    #return testRequest()

    