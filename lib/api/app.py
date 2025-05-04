from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from lib.api.routes.router import router

app = FastAPI(
    title="LLM News API",
    description="A simple API to get the latest news from various sources.",
    docs_url="/api",
)

app.include_router(router, prefix="/api")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/api")
