import datetime
from typing import Union

from fastapi import APIRouter, Cookie, Depends, Request, Header, Security
from starlette.requests import Request
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.api.core.config import settings
from app.api.db.mongodb import AsyncIOMotorCollection, get_collection
from urllib.parse import quote_plus, urlencode
from app.authentication import JWTBearer
from app.api.models.game_schema_model import GameSchema

from app.api.services.game_schema_service import create_schema_service
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/")
async def gamification_home(request: Request, collection: AsyncIOMotorCollection = Depends(get_collection)):
    """
    WIP
    """
    try:
        return {
            "message": "Welcome to the Gamification API",
            
        }
    except Exception as err:
        print(err)
        raise err  

# test user is logged /test_logged 


@router.post("/", dependencies=[Depends(JWTBearer())])
async def create_game_schema(game_schema: GameSchema):
    """
    Create a game schema
    """
    try:
        game_schema_created = await create_schema_service(game_schema)
        return {
            "message": "Game schema created successfully",
            "game_schema_id": str(game_schema_created.inserted_id)
        }
    except Exception as err:
        print(err)
        raise err
    