import jwt

from key import get_jwk_set
from models.PebbleAuthToken import PebbleAuthToken
from token import get_token_data_from_jwt_payload


def auth(token: str) -> PebbleAuthToken:
    """
    Authenticate a provided token into and return a valid PebbleAuthToken object
    :param token: str
    :return: PebbleAuthToken
    """
    jwks = get_jwk_set()

    algorithm = jwt.get_unverified_header(token).get('alg')

    data = jwt.decode(token=token,
                      key=jwks,
                      algorithms=algorithm)

    token_data = get_token_data_from_jwt_payload(data, token)

    return PebbleAuthToken(token_data)
