from datatypes.AuthenticatedLicenceObject import AuthenticatedLicenceObject
from datatypes.PebbleTokenData import PebbleTokenData
from datatypes.UserObject import UserObject
from models.PebbleAuthToken import PebbleAuthToken
from models.User import User


def get_licence_object_from_token_data(token_data: PebbleTokenData) -> AuthenticatedLicenceObject:
    auth_token = PebbleAuthToken(token_data)
    user = User(
        UserObject(username=token_data.sub, roles=token_data.roles, level=token_data.lv, display_name=token_data.name))
    return AuthenticatedLicenceObject(app=token_data.aud, id=token_data.iss, tenant_id=token_data.tid, token=auth_token,
                                      user=user)


def get_token_data_from_jwt_payload(jwt_payload: any, token: str) -> PebbleTokenData:
    return PebbleTokenData(aud=jwt_payload.aud,
                           iss=jwt_payload.iss,
                           tid=jwt_payload.tid,
                           sub=jwt_payload.sub,
                           roles=jwt_payload.roles,
                           lv=jwt_payload.lv,
                           name=jwt_payload.name,
                           iat=jwt_payload.iat,
                           exp=jwt_payload.exp,
                           token=token)
