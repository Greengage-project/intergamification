import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from app.api.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 10

client = AsyncIOMotorClient(settings.MONGODB_URL)


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def wait_for_database() -> None:
    try:
        collection = client[settings.MONGODB_DATABASE][settings.COLLECTION_NAME_GAME_SCHEMA]
        collection.find_one({"_id": "TEST"})
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    wait_for_database()
    logger.info("Services finished initializing")
    client.close()


if __name__ == "__main__":
    main()
