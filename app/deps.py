from fastapi import Security
# jwt token
from app.authentication import JWTBearer

JWTBearer = JWTBearer()


async def get_current_user(token: str = Security(JWTBearer)):
    print('get_current_user')
    print(token)
    return token
