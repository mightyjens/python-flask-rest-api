import os, re, json 
import logging, logging.config

from common.logdna import LOGGING
from flask import Flask, request
from werkzeug.security import generate_password_hash

# Define routes
# https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like

# Import the blueprint from versions
from v1.routes import api as api_v1
from v2.routes import api as api_v2

app = Flask(__name__)

# Now register the blueprint with url prefix
app.register_blueprint(api_v1, url_prefix='/v1')
app.register_blueprint(api_v2, url_prefix='/v2')

# Logging setup
app.config['LOGGER_HANDLER_POLICY'] = os.environ['LOG_POLICY']
app.logger 

logging.config.dictConfig(LOGGING)

# Show available versions
@app.route('/')
def index():
    path = '.'
    listVersions = []
    directoryContents = os.listdir(path)

    # List api versions 
    for item in directoryContents:
        if os.path.isdir(item):
            if re.match('v[1-9]', item):
                listVersions.append(item)

    return json.dumps(listVersions), 200

# Generate password hash for api users
@app.route('/passwordhash', methods=["GET"])
def generatePassword():
    password = request.args.get('password')

    # Return the hashed password
    if password:
        return generate_password_hash(password).replace(os.environ["ENCRYPTION_HASH_PREFIX"],''), 200
    else:
        return '', 400