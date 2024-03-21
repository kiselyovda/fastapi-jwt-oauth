from typing import Annotated

from fastapi import Depends

from authorization.auth.exceptions import token_exc
from authorization.schemas import Payload
from authorization.users import utils as user_utils
from authorization.users.schemas import BaseUser, UserInDB
from authorization.utils import get_token_payload
from db_example import users_db


def get_current_user(
    payload: Annotated[Payload, Depends(get_token_payload)]
) -> BaseUser:
    username = payload.get("username", "")
    if user := users_db.get(username):
        return BaseUser(**user.model_dump())
    raise token_exc


def get_user(username: str):
    if username in users_db:
        user_dict = users_db[username]
        return UserInDB(**user_dict.model_dump())


def authenticate_user(username: str, password: str) -> BaseUser:
    user = get_user(username)
    if not user:
        raise Exception
    if not user_utils.validate_password(password, user.hashed_password):
        raise Exception
    return user
