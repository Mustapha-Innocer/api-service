from fastapi import APIRouter

from lib.api.routes.routers.story import router as story_router

router = APIRouter()

router.include_router(story_router, prefix="/stories", tags=["Story"])
