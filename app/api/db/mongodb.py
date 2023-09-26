import logging
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from app.api.core.config import settings
import os

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    return db.client[settings.MONGODB_DATABASE][collection_name]


async def connect_to_mongo():
    logging.info("Connecting to database...")
    db.client = AsyncIOMotorClient(
        settings.MONGODB_URL,
        maxPoolSize=MAX_CONNECTIONS_COUNT,
        minPoolSize=MIN_CONNECTIONS_COUNT,
    )
    logging.info("Database connected！")


async def close_mongo_connection():
    logging.info("Closing database connection...")
    db.client.close()
    logging.info("Database closed！")
