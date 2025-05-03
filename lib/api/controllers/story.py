from sqlalchemy.orm import Session

from lib.db.crud import story_crud


def get_top_stories(db: Session, limit: int = 10):
    """
    Get the top stories from the database.
    """
    return story_crud.get_top_stories(db, limit)
