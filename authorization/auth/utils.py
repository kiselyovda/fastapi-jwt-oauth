from datetime import datetime, timedelta, timezone

import jwt

from authorization.auth.config import auth_config as config


def _expire(
    expire_minutes: int = config.access_token_expire_minutes,
    *,
    expire_timedelta: timedelta | None = None,
) -> tuple[datetime, datetime]:
    now = datetime.now(timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    return now, expire


def encode_jwt(
    payload: dict,
    *,
    private_key: str = config.private_key,
    algorithm: str = config.algorithm,
    expire_minutes: int = config.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now, expire = _expire(
        expire_minutes=expire_minutes, expire_timedelta=expire_timedelta
    )
    to_encode.update(exp=expire, iat=now)
    return jwt.encode(payload=to_encode, key=private_key, algorithm=algorithm)


def decode_jwt(
    token: str | bytes,
    *,
    public_key: str = config.public_key,
    algorithm: str = config.algorithm,
):
    return jwt.decode(jwt=token, key=public_key, algorithms=[algorithm])
