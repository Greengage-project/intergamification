from app.api.db.mongodb import get_collection
from app.api.models.game_instance_model import GameBase
from app.api.core.config import settings


async def get_all_games():
    collection = await get_collection(settings.COLLECTION_NAME_GAMES_INSTANCES)
    games = []
    async for game in collection.find():
        games.append(game)
    return games


async def get_game_by_process_id(process_id: str):
    collection = await get_collection(settings.COLLECTION_NAME_GAMES_INSTANCES)
    game = await collection.find_one({"process_id": process_id})
    return game


async def add_game(game: GameBase):
    collection = await get_collection(settings.COLLECTION_NAME_GAMES_INSTANCES)
    game_data = game.dict()
    await collection.insert_one(game_data)
    return game_data
