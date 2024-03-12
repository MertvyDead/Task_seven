from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models as models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from routes import router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(router, prefix="/user", tags=["user"])
    