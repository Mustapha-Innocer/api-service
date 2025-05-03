from lib.db.Base import Story
from lib.logging.logger import LOGGER


def get_top_stories(db, limit=10):
    """
    Get the top stories from the database.
    """
    LOGGER.info("Fetching top stories from the database.")
    return db.query(Story).order_by(Story.published_at.desc()).limit(limit).all()
