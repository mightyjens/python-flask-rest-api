from flask import Flask

# Define routes
# https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like
from v1.routes import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/v1')

