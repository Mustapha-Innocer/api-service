from lib.db.Base import Source
from lib.logging.logger import LOGGER


def get_all_sources(db):
    """
    Get all news sources.
    """
    LOGGER.info("Getting all sources")
    return db.query(Source).all()
