import os, common.mongo, common.functions
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password) -> str:
    # Check username is filled
    if not username:
        return None
    
    # Check environmental logins
    passwordResponse = common.functions.getValueFromEnv(username)

    if not passwordResponse:
        # Fetch data from cosmos db
        passwordResponse = common.mongo.getUserFromDatabase(username)
        if not passwordResponse:
            return None

    encryptionSalt = os.environ["ENCRYPTION_SALT"]

    if check_password_hash(f"{encryptionSalt}{passwordResponse}", password):
        return username
    else:
        return None