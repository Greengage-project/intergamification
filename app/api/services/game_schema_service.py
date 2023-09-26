from app.api.db.mongodb import get_collection, AsyncIOMotorCollection
from app.api.models.game_schema_model import GameSchema
from app.api.core.config import settings

async def create_schema_service(game_schema: GameSchema):
    game_schema_collection: AsyncIOMotorCollection = await get_collection(settings.COLLECTION_NAME_GAME_SCHEMA)
    
    # Convertir action_reward_due_date a cadena
    for action_reward in game_schema.actions_rewards:
        if action_reward.action_reward_due_date is not None:
            action_reward.action_reward_due_date = action_reward.action_reward_due_date.isoformat()
            
    # Insertar en MongoDB
    game_schema_created = await game_schema_collection.insert_one(game_schema.dict())
    return game_schema_created
