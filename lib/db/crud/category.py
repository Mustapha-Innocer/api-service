from sqlalchemy.orm import Session

from lib.db.models.Category import Category
from lib.logging.logger import LOGGER


def get_categories(db: Session, limit: int | None) -> list[Category]:
    """
    Get all categories from the database.
    """
    LOGGER.info("Fetching all categories from the database.")
    if limit is not None:
        return db.query(Category).limit(limit).all()

    return db.query(Category).all()
