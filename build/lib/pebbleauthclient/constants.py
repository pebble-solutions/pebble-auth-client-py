import os

"""
Return the location of remote pebble authenticator public keys set (JWKS) as defined in the sys global
environment variables
"""
JWKS_REMOTE_URI: str = os.getenv('PBL_JWKS_REMOTE_URI')

"""
Contains the local folder for temporary store authentication credentials. Storing locally the credentials improves
server response.
"""
CERTS_FOLDER: str = "./var/credentials/auth"

"""
Contains the local path for the public keys set (JWKS)
"""
JWKS_LOCAL_PATH: str = CERTS_FOLDER + "/jwks.json"
