from dataclasses import dataclass
from models.User import User
from models.PebbleAuthToken import PebbleAuthToken


@dataclass
class AuthenticatedLicenceObject:
    app: str
    id: str
    tenant_id: str
    token: PebbleAuthToken
    user: User
