from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from authorization.auth.exceptions import unauthed_exc
from authorization.auth.schemas import TokenInfo
from authorization.auth import utils as auth_utils
from authorization.users.services import authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> TokenInfo:
    user = authenticate_user(username=form_data.username, password=form_data.password)
    if not user:
        raise unauthed_exc
    payload = {"sub": user.username, "username": user.username}
    token = auth_utils.encode_jwt(payload=payload)
    return TokenInfo(access_token=token)
