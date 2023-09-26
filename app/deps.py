from fastapi import HTTPException, Request, Depends, Security
# jwt token
from fastapi.security import OAuth2AuthorizationCodeBearer
from app.authentication import JWTBearer

JWTBearer = JWTBearer()

async def get_current_user(token: str = Security(JWTBearer)):
    print('get_current_user')
    print(token)
    return token
