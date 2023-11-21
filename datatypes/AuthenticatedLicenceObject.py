import dataclasses
import models.User as UserModel
import models.PebbleAuthToken as PebbleAuthTokenModel


@dataclasses.dataclass
class AuthenticatedLicenceObject:
    app: str
    id: str
    tenant_id: str
    token: PebbleAuthTokenModel.PebbleAuthToken
    user: UserModel.User
