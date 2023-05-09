from fastapi import FastAPI
import models
from routes import router
from routechapter import router_chapters
from upload_chapters import router_upload
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# mode
# app.include_router(router, prefix="/book", tags=["book"])
app.include_router(router, prefix="/manga", tags=["manga"])
app.include_router(router_chapters, prefix="/chapters", tags=["chapters"])
app.include_router(router_upload, prefix="/upload", tags=["upload"])
