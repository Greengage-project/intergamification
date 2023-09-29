from typing import Optional
from datetime import datetime
from pydantic import BaseModel, UUID4


class JWT_data(BaseModel):
    exp: Optional[datetime] = None
    iat: Optional[datetime] = None
    auth_time: Optional[datetime] = None
    jti: Optional[str] = None
    iss: Optional[str] = None
    aud: Optional[str] = None
    sub: Optional[UUID4] = None
    typ: Optional[str] = None
    azp: Optional[str] = None
    nonce: Optional[str] = None
    session_state: Optional[str] = None
    at_hash: Optional[str] = None
    acr: Optional[str] = None
    sid: Optional[str] = None
    email_verified: Optional[bool] = None
    name: Optional[str] = None
    preferred_username: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
