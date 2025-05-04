from sqlalchemy.orm import Session

from lib.db.crud import source as source_crud


def get_sources(
    db: Session,
    limit: int | None = None,
):
    """
    Get list of sources from the database.
    """
    return source_crud.get_sources(db, limit)
