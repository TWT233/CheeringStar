from . import models
from .init import get_db, engine

models.Base.metadata.create_all(bind=engine)
