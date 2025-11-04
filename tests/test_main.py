from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from app.main import app 
import pytest
@pytest.fixture
def patient():
     return {
  "age": 20,
  "gender": 1,
  "pressurehight": 14,
  "pressurelow": 15,
  "glucose": 12,
  "kcm": 1.3,
  "troponin": 1.2,
  "impluse": 7
}
client= TestClient(app)
def test_predict_status(patient):
     response = client.post("/predict_risk", json =patient)
     assert response.status_code == 200