from datetime import datetime

from typing import TypedDict


class Payload(TypedDict):
    username: str
    hashed_password: bytes
    exp: datetime
    iat: datetime
