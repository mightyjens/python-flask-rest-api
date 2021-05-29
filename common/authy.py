import os, common.mongo, common.functions
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password) -> str:
    # Check username is filled
    if not username:
        return None
    
    # Check for environmental logins
    passwordResponse = common.functions.getValueFromEnv(username)

    if not passwordResponse:
        # Fetch data from cosmos db
        passwordResponse = common.mongo.getUserFromDatabase(username)
        if not passwordResponse:
            return None

    encryptionHashPrefix = os.environ["ENCRYPTION_HASH_PREFIX"]

    if check_password_hash(f"{encryptionHashPrefix}{passwordResponse}", password):
        return username
    else:
        return None