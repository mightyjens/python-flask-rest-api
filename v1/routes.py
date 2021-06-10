#from common.logdna import logDna
import common.logdna as logger


from .functions import checkRuntime, checkVersion
from common.authy import auth
from flask import Blueprint

api = Blueprint('api_v1', __name__)

@api.route('/', methods=["GET"])
@auth.login_required
def index():
    return f"{checkVersion()} on {checkRuntime()}"
