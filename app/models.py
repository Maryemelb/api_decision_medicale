from pydantic import BaseModel
from sqlalchemy import Column, Integer, create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from unittest.mock import Base
from sqlalchemy import Float 
from sqlalchemy.ext.declarative import declarative_base

# #Database setup
# Database_url= 'sqlite:///./database.db'
# engine = create_engine(Database_url)
# sessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)
Base = declarative_base()

class Patient(Base):
    __tablename__= "patients"
    id = Column(Integer, primary_key=True, index=True)
    age= Column(Integer, nullable= False)
    gender=Column(Integer, nullable= False)
    pressurehight=Column(Integer, nullable= False)
    pressurelow = Column(Integer, nullable=False)
    glucose=Column(Integer, nullable=False)
    kcm= Column(Float, nullable=False)
    troponin=Column(Float, nullable=False)
    impluse = Column(Integer,nullable=False)