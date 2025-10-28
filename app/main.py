from fastapi import FastAPI
app= FastAPI()
@app.get('/')
async def index():
    return "hello"
@app.get('/prediction')
async def prediction():
    return "pred"