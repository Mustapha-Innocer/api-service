from sqlalchemy.orm import Session

from lib.db.Base import Category, Source, Story
from lib.logging.logger import LOGGER


def get_top_stories(
    db: Session,
    limit: int,
    source: str | None = None,
    category: str | None = None,
) -> list[Story]:
    """
    Get the top stories from the database.
    """
    LOGGER.info("Fetching top stories from the database.")

    if source and category:
        query = (
            db.query(Story)
            .join(Story.category)
            .join(Story.source)
            .filter(
                Source.name == source,
                Category.name == category,
            )
        )

    elif source:
        query = (
            db.query(Story)
            .join(Story.source)
            .filter(
                Source.name == source,
            )
        )

    elif category:
        query = (
            db.query(Story)
            .join(Story.category)
            .filter(
                Category.name == category,
            )
        )
    else:
        query = db.query(Story)

    return query.order_by(Story.published_at.desc()).limit(limit).all()
