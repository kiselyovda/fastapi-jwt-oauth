from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


CREDENTIALS = Path(__file__).parent.parent.parent / "credentials"


class AuthConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=False, extra="ignore", secrets_dir=CREDENTIALS
    )

    private_key: str = Field(alias="jwt-private.pem")
    public_key: str = Field(alias="jwt-public.pem")
    algorithm: str
    access_token_expire_minutes: int


auth_config = AuthConfig()
