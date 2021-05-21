import v1.functions
import common.functions

from flask import Blueprint

api = Blueprint('api_v1', __name__)

@api.route('/')
def index():
    return common.functions.helloworld()

@api.route('/checkversion')
def checkVersion():
    return v1.functions.checkVersion()