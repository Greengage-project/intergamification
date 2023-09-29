
from bson import ObjectId
from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordBearer
from app.authentication import JWTBearer
from app.api.models.game_instance_model import GameBase, NewGameBody
from app.api.services.game_service import add_game, get_all_games, get_game_by_process_id
from app.api.services.game_schema_service import get_game_schema_by_id_service
from app.api.models.default_data_model import default_new_game_instance

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


@router.post("/", dependencies=[Depends(JWTBearer())])
async def add_game_instance(token: str = Depends(JWTBearer()), game_instance: NewGameBody = Body(..., example=default_new_game_instance)):
    """
    Create a game instance
    """
    try:
        # check if game_schema_id is a valid ObjectId
        if not ObjectId.is_valid(game_instance.gameSchema_id):
            return {
                "message": "Invalid game schema id"
            }
        # check if game_schema_id exists
        game_schema = await get_game_schema_by_id_service(game_instance.gameSchema_id)
        if not game_schema:
            return {
                "message": "Game schema not found"
            }
        # check if exist anothe game instance with the same process_id and status = active
        game_instance_exist = await get_game_by_process_id(game_instance.processId)
        if game_instance_exist:
            return {
                "message": "Game instance already exists for this process_id"
            }
        # create game instance
        jwt_bearer = JWTBearer()
        data_token = jwt_bearer.decode_token(token)
        new_game = GameBase(
            process_id=game_instance.processId,
            gameSchema=game_schema,
            createdBy=data_token,
            status="active",
            dataGame=[]
        )
        # add game instance to database
        game_instance_created = await add_game(new_game)
        return {
            "message": "Game instance created successfully",
            "game_instance_id": str(game_instance_created.inserted_id)
        }
    except Exception as err:
        print(err)
        raise err
