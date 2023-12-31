from bson import ObjectId
from app.api.db.mongodb import get_collection, AsyncIOMotorCollection
from app.api.models.game_schema_model import GameSchemaBase
from app.api.core.config import settings


async def create_schema_service(game_schema: GameSchemaBase):
    game_schema_collection: AsyncIOMotorCollection = await get_collection(settings.COLLECTION_NAME_GAME_SCHEMA)
    # Insertar en MongoDB
    game_schema_created = await game_schema_collection.insert_one(game_schema.dict())
    return game_schema_created

# get all game schemas


async def get_all_game_schemas_service():
    game_schema_collection: AsyncIOMotorCollection = await get_collection(settings.COLLECTION_NAME_GAME_SCHEMA)
    game_schemas = []
    async for game_schema in game_schema_collection.find():
        # Convertir ObjectId a str antes de agregarlo a la lista
        game_schema["_id"] = str(game_schema["_id"])
        game_schemas.append(game_schema)
    return game_schemas


async def get_game_schema_by_id_service(game_schema_id: str):
    game_schema_collection: AsyncIOMotorCollection = await get_collection(settings.COLLECTION_NAME_GAME_SCHEMA)
    game_schema = await game_schema_collection.find_one({"_id": ObjectId(game_schema_id)})
    if (not game_schema):
        return None
    # Convertir ObjectId a str antes de devolverlo
    game_schema["_id"] = str(game_schema["_id"])
    return game_schema
