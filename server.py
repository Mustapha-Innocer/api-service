import uvicorn

from lib.api.app import app
from lib.config import config

options = {
    "host": config.HOST,
    "port": config.PORT,
}

if __name__ == "__main__":
    if config.ENV == "DEV":
        uvicorn.run(
            app="server:app",
            reload=True,
            **options,
        )
    elif config.ENV == "TEST":
        uvicorn.run(
            app=app,
            **options,
        )
    else:
        uvicorn.run(
            app="server:app",
            **options,
        )
