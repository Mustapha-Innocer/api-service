from fastapi import APIRouter

from lib.api.routes.routers.category import router as category_router
from lib.api.routes.routers.story import router as story_router
from lib.api.routes.routers.source import router as source_router

router = APIRouter()

router.include_router(story_router, prefix="/stories", tags=["News"])
router.include_router(category_router, prefix="/categories", tags=["News"])
router.include_router(source_router, prefix="/sources", tags=["News"])
