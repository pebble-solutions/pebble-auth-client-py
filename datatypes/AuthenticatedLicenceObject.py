from dataclasses import dataclass
import models.User as UserModel


@dataclass
class AuthenticatedLicenceObject:
    app: str
    id: str
    tenant_id: str
    user: UserModel.User
