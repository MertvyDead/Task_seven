from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from crud import UserSchema, Request, Response, RequestUser
from typing import List, Annotated

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session,Depends(get_db)]


@router.post("/create")
def create_user_service(request: RequestUser, db: Session = Depends(get_db)):
    crud.create_user(db, user=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="User created successfully").dict(exclude_none=True)


@router.get("/")
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=users)


@router.patch("/update")
def update_users(request: RequestUser, db: Session = Depends(get_db)):
    user  = crud.update_user(db, user_id=request.parameter.id,
                             login=request.parameter.login, password=request.parameter.password)
    return Response(status="Ok", code="200", message="Success update data", result=user)


@router.delete("/delete")
def delete_user(request: RequestUser,  db: Session = Depends(get_db)):
    crud.del_user(db, user_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

