from fastapi import FastAPI
from backend.database import Base,engine
from backend.routers.auth import router as auth_router
from backend.models.user import User

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(auth_router)