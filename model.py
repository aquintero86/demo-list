from db import Base
from sqlalchemy import Column, Integer, String 

#Mapping user's table and its columns 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    