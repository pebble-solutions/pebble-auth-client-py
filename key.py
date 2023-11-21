import os.path
import json

import constants
from errors import EmptyJWKSRemoteURIError, EmptyJWKSError


def get_jwk_set():
    pass

def import_remote_jwks(remote_location: str):
    pass

def read_jwks():
    if os.path.isfile(constants.JWKS_LOCAL_PATH):
        if not constants.JWKS_REMOTE_URI:
            raise EmptyJWKSRemoteURIError()
        import_remote_jwks(constants.JWKS_REMOTE_URI)

    with open(constants.JWKS_LOCAL_PATH) as f:
        data = f.read()

    if not data:
        raise EmptyJWKSError()

    return json.loads(data)