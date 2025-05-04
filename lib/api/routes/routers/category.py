from fastapi import APIRouter, Depends

from lib.api.controllers import category as controller
from lib.db.session import get_db

router = APIRouter()


@router.get(
    "/",
    description="List all available categories",
    response_model=list[str],
)
async def query_categories(
    limit: int | None = None,
    db=Depends(get_db),
):
    return controller.get_categories(db, limit)
