
from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordBearer
from app.authentication import JWTBearer
from app.api.models.game_instance_model import Game
from app.api.services.game_service import get_all_games

from app.api.models.default_data_model import default_game_schema

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
async def get_all_games_instances():
    """
    Get all game instances
    """
    try:
        games = await get_all_games()
        return {
            "games": games
        }
    except Exception as err:
        print(err)
        raise err
