
import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import PyJWKClient
from app.api.core.config import settings

class JWTBearer(HTTPBearer):
    def __ini__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        
    def verify_jwt(self, jwtoken: str) -> bool:
        try:
            jwks_client = PyJWKClient(settings.KEYCLOAK_URL_REALM + "/protocol/openid-connect/certs")
            signing_key = jwks_client.get_signing_key_from_jwt(jwtoken)
            data = jwt.decode(
                jwtoken,
                signing_key.key,
                algorithms=["RS256"],
                audience=settings.KEYCLOAK_CLIENT_ID,
                # options={"verify_nbf": False},
            )
            return True
        except:
            return False
        
    def decode_token(self, jwtoken):
        jwks_client = PyJWKClient(settings.KEYCLOAK_URL_REALM + "/protocol/openid-connect/certs")
        signing_key = jwks_client.get_signing_key_from_jwt(jwtoken)
        data = jwt.decode(
            jwtoken,
            signing_key.key,
            algorithms=["RS256"],
            audience=settings.KEYCLOAK_CLIENT_ID,
            # options={"verify_nbf": False},
        )
        return data
    