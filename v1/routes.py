import os
from v1.functions import checkRuntime, checkVersion
from common.authy import auth
from flask import Blueprint

api = Blueprint('api_v1', __name__)

@api.route('/')
def index():
    return f"{checkVersion()} on {checkRuntime()}"
