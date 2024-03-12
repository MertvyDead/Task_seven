from sqlalchemy.orm import Session
from models import User
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel


T = TypeVar('T')


class UserSchema(BaseModel):
    id: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

def get_user(db:Session, skip: int = 0, limit: int = 100 ):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db:Session,user_id: int):
    return db.query(User).filter(User.id ==user_id).first()

def create_user(db: Session,user: UserSchema ):
    _user = User(login = user.login, password = user.password)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def del_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id = user_id)
    db.delete(_user)
    db.commit
    
def update_user(db: Session, user_id: int, login: str, password: str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.login=login
    _user.password = password
    db.commit()
    db.refresh(_user)
    
    return _user