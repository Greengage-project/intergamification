from app.api.db.mongodb import get_collection
from app.api.models import Game

async def add_game(game: Game):
    collection = await get_collection()
    game_data = game.dict()
    await collection.insert_one(game_data)
    return game_data
