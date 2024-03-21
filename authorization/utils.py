from typing import Annotated

from fastapi import Depends
from jwt import InvalidTokenError

from authorization.auth import utils as auth_utils
from authorization.auth.exceptions import token_exc
from authorization.dependencies import oauth_scheme
from authorization.schemas import Payload


def get_token_payload(token: Annotated[str, Depends(oauth_scheme)]) -> Payload:
    try:
        payload = auth_utils.decode_jwt(token=token)
    except InvalidTokenError:
        raise token_exc
    return payload
