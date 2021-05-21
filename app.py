import os
import re
import json
from flask import Flask

# Define routes
# https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like
from v1.routes import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/v1')

# Set base url content
@app.route('/')
def index():
    path = '.'
    list_versions = []
    directory_contents = os.listdir(path)

    for item in directory_contents:
        if os.path.isdir(item):
            if re.match('v[1-9]', item):
                list_versions.append(item)

    return json.dumps(list_versions)
