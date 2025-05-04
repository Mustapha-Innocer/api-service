from sqlalchemy.orm import Session

from lib.db.crud import category as category_crud


def get_categories(
    db: Session,
    limit: int | None = None,
):
    """
    Get list of categories from the database.
    """
    categories = category_crud.get_categories(db, limit)
    return [categories.name for categories in categories]
