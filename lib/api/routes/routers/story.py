from fastapi import APIRouter, Depends

from lib.api.controllers import story as controller
from lib.api.schemas.Story import Story
from lib.db.session import get_db

router = APIRouter()


@router.get("/", description="Get all top stories", response_model=list[Story])
async def query_top_stories(
    limit: int = 10,
    category: str | None = None,
    source: str | None = None,
    db=Depends(get_db),
):
    return controller.get_top_stories(db, limit, category, source)
