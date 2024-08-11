from fastapi import FastAPI


app = FastAPI()

@app.get("/test")
def index():
    return {"name": "First Data"}

