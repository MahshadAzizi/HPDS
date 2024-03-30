from fastapi import FastAPI
from app.config.celery_utils import create_celery   # new


def create_app() -> FastAPI:
    app = FastAPI()

    # do this before loading routes              # new
    app.celery_app = create_celery()  # new

    from app.ram import ram_router
    app.include_router(ram_router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app
