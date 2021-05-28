import common.mongo
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password) -> str:
    
    # Fetch data from cosmos db
    passwordResponse = common.mongo.getUserFromDatabase(username)
    if not passwordResponse:
        return None

    if check_password_hash(f"pbkdf2:sha256:260000${passwordResponse}", password):
        return username
    else:
        return None
