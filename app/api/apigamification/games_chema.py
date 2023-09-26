
from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordBearer
from app.authentication import JWTBearer
from app.api.models.game_schema_model import GameSchema
from app.api.services.game_schema_service import create_schema_service, get_all_game_schemas_service

from app.api.models.default_data_model import default_game_schema

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
async def get_all_game_schemas():
    """
    Get all game schemas
    """
    try:
        game_schemas = await get_all_game_schemas_service()
        return {
            "game_schemas": game_schemas
        }
    except Exception as err:
        print(err)
        raise err


# test user is logged /test_logged


@router.post("/", dependencies=[Depends(JWTBearer())])
async def create_game_schema(game_schema: GameSchema = Body(..., example=default_game_schema)):
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
