from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class User(Base):
     __tablename__ = 'user'
     id = Column(Integer, primary_key=True, index=True)
     user_name = Column(String, unique=True, index=True)
     full_name = Column(String, unique=True, index=True)
     email = Column(String, unique=True, index=True, nullable=False)
     hashed_password = Column(String, nullable=False)



class Red_flag(Base):
     __tablename__ = 'redflag'
     id = Column(Integer, primary_key=True, index=True)

     