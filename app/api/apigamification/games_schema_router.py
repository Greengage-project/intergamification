
from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordBearer
from app.authentication import JWTBearer
from app.api.models.game_schema_model import GameSchema
from app.api.services.game_schema_service import create_schema_service, get_all_game_schemas_service, get_game_schema_by_id_service

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


@router.post("/", dependencies=[Depends(JWTBearer())])
async def create_game_schema(token: str = Depends(JWTBearer()), game_schema: GameSchema = Body(..., example=default_game_schema)):
    """
    Create a game schema
    """
    try:
        jwt_bearer = JWTBearer()
        data_token = jwt_bearer.decode_token(token)
        game_schema.created_by = data_token
        game_schema_created = await create_schema_service(game_schema)
        return {
            "message": "Game schema created successfully",
            "game_schema_id": str(game_schema_created.inserted_id)
        }
    except Exception as err:
        print(err)
        raise err

# get game schema by id
# game_schema_id bson.errors.InvalidId: '6512e25596d12917df1820c63' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string


@router.get("/{game_schema_id}")
async def get_game_schema_by_id(game_schema_id: str):
    """
    Get a game schema by id
    """
    try:
        # check if game_schema_id is a valid ObjectId
        if not ObjectId.is_valid(game_schema_id):
            return {
                "message": "Invalid game schema id"
            }
        game_schema = await get_game_schema_by_id_service(game_schema_id)
        if (not game_schema):
            # return with 404 status code if game schema not found
            return {
                "message": "Game schema not found"
            }

        return {
            "game_schema": game_schema
        }
    except Exception as err:
        print(err)
        raise err
