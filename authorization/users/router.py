from typing import Annotated
from fastapi import APIRouter, Depends

from authorization.schemas import Payload
from authorization.utils import get_token_payload
from authorization.users.services import get_current_user
from authorization.users.schemas import BaseUser

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def me(
    payload: Annotated[Payload, Depends(get_token_payload)],
    user: Annotated[BaseUser, Depends(get_current_user)],
):
    return {"username": user.username, "iat": payload.get("iat"), "user": user}


@router.get("/username")
async def username(
    payload: Annotated[Payload, Depends(get_token_payload)]
) -> dict[str, str]:
    return {"message": "success", "username": payload.get("username", "")}
