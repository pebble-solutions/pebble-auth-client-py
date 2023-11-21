from dataclasses import dataclass
from typing import Sequence


@dataclass
class UserObject:
    username: str
    display_name: str
    level: int
    roles: Sequence[str]
