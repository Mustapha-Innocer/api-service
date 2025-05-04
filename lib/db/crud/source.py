from sqlalchemy.orm import Session

from lib.db.Base import Source
from lib.logging.logger import LOGGER


def get_sources(db: Session, limit: int | None) -> list[Source]:
    """
    Get news sources.
    """
    LOGGER.info("Reading sources from db")
    if limit is not None:
        return db.query(Source).order_by(Source.name).limit(limit)

    return db.query(Source).order_by(Source.name).all()
