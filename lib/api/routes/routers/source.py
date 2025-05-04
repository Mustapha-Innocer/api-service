from fastapi import APIRouter, Depends

from lib.api.controllers import source as controller
from lib.api.schemas.Source import Source
from lib.db.session import get_db

router = APIRouter()


@router.get(
    "/",
    description="Get News source",
    response_model=list[Source],
)
async def query_sources(
    limit: int | None = None,
    db=Depends(get_db),
):
    return controller.get_sources(db, limit)
