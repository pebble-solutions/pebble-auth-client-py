from User import User
from PebbleAuthToken import PebbleAuthToken
from datatypes.AuthenticatedLicenceObject import AuthenticatedLicenceObject


class AuthenticatedLicence(AuthenticatedLicenceObject):

    def __init__(self, token_object: AuthenticatedLicenceObject):
        self.app: str = token_object.app
        self.id: str = token_object.id
        self.tenant_id: str = token_object.tenant_id
        self.token: PebbleAuthToken = token_object.token
        self.user: User = token_object.user

    def get_token(self) -> PebbleAuthToken:
        return self.token

    def get_user(self) -> User:
        return self.user
