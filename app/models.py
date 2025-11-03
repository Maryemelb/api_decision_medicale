import sqlalchemy
from sqlalchemy import Column, Integer
from sqlalchemy import Float 
from app.database import Base

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