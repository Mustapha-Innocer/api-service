from sqlalchemy.orm import Session

from lib.db.crud import story


def get_top_stories(
    db: Session,
    limit: int,
    category: str | None = None,
    source: str | None = None,
):
    """
    Get the top stories from the database.
    """
    return story.get_top_stories(db, limit, source, category)
