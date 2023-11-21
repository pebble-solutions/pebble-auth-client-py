from dataclasses import dataclass
from typing import Sequence


@dataclass
class PebbleTokenData:
    aud: str
    exp: int
    iat: int
    iss: str
    lv: int
    name: str
    roles: Sequence[str];
    sub: str
    tid: str
    token: str
