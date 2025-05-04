from sqlalchemy.orm import Session

from lib.db.crud import story_crud


def get_top_stories(db: Session, limit: int):
    """
    Get the top stories from the database.
    """
    return story_crud.get_top_stories(db, limit)
