from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import  Session
from app.models import Patient
from app.database import engine,sessionLocal, Base
import joblib 
import pandas as pd
from fastapi import FastAPI

app= FastAPI(title='api prediction')
Base.metadata.create_all(bind=engine)

class Create_Patient(BaseModel):
    age: int
    gender:int
    pressurehight: int
    pressurelow: int
    glucose: int
    kcm: float
    troponin: float
    impluse: int
class get_patient(BaseModel):
    # id = int
    age: int
    gender:int
    pressurehight: int
    pressurelow: int
    glucose: int
    kcm: float
    troponin: float
    impluse: int

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close

@app.get('/')
async def index():
    return "hello"

@app.post('/patients')
async def add_patient(patient: Create_Patient, db:Session= Depends(get_db)):
        db_item=Patient(**patient.model_dump()) #returns a dictionary of the fields and their values
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

@app.get('/patient')
async def get_patients(db: Session= Depends(get_db)):
     item=db.query(Patient).all()
     if item is None:
          raise HTTPException(status_code=404, detail="item not found")
     return item
@app.post('/predict_risk')
async def predict_status(patient: Create_Patient):
    model= joblib.load('app/classification_model.pkl')  
    #patient is a pandantic object
    # data= patient.values()
    data= pd.DataFrame([patient.dict()])
    predict1= model.predict(data)
    print("prediction",predict1)
    if predict1==1:
        return "Ce patient est a risque élevé d'avoir une maladi cardiovasculaire"
    else:
        return "Ce patient n a pas de risque d'avoir une maladi cardiovasculaire"

     

