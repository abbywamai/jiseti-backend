from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
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
    role = Column(String, nullable=False)

    red_flags = relationship('Red_flag', back_populates='user')
    interventions = relationship('Intervention', back_populates='user')

# class Red_flag(Base):
#     __tablename__ = 'redflag'
#     id = Column(Integer, primary_key=True, index=True)
#     incident_type = Column(String)
#     description = Column(String, nullable=False)
#     additional_details = Column(String)
#     latitude = Column(Float)
#     longitude = Column(Float)
#     userid = Column(Integer, ForeignKey('user.id'))
#     statusid = Column(Integer, ForeignKey('status.id'))

#     user = relationship('User', back_populates='red_flags')

# class Intervention(Base):
#     __tablename__ = 'interventions'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     latitude = Column(Float)
#     longitude = Column(Float)
#     userid = Column(Integer, ForeignKey('user.id'))
#     statusid = Column(Integer, ForeignKey('status.id'))

#     user = relationship('User', back_populates='interventions')

# class Status(Base):
#     __tablename__ = 'status'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)

#     red_flags = relationship('Red_flag', back_populates='status')
#     interventions = relationship('Intervention', back_populates='status')
