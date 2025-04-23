from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
        title="FastAPI Template",
        docs_url="/api",
    )


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/api")
