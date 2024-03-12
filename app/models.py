from sqlalchemy import Boolean, Integer, ForeignKey, String, Column
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key= True)
    login = Column(String, unique= True)
    password = Column(String)
    
