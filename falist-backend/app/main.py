from fastapi import FastAPI
from .database import engine
from . import models
from .controllers import item_controller


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="falist")

app.include_router(item_controller.router)


@app.get("/health")
def health():
    return {"status": "ok", "name": "falist"}
