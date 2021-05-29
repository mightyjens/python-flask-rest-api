import os
import re
import json
from flask import Flask, request
from werkzeug.security import generate_password_hash

# Define routes
# https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like
from v1.routes import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/v1')

# Set base url content
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

@app.route('/passwordhash', methods=["GET"])
def generatePassword():
    password = request.args.get('password')

    # Return the hashed password
    if password:
        return generate_password_hash(password).replace(os.environ["ENCRYPTION_SALT"],''), 200
    else:
        return '', 400