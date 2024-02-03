from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root(): # ini hanya menampilkan root url saja seperti 127.0.0.1:8000
    return {"Hello": "Apa Kabar"}

@app.post("/predict") # nah kalau ini ada penambahan pada url nya seperti 127.0.0.1:8000/predict
def predict():
    return {"Predicted": "Virginica Iris"}

@app.post("/greetings")
async def greetings(request: Request):
    data = await request.json()
    result = f"Hello {data["name"]}"
    return {"Greetings": result}
