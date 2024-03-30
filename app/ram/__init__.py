from . import api
ram_router = api.router

from . import models, tasks, schemas, crud  # noqa
from ..config.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
