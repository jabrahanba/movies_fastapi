from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000 ruta raiz local

@app.get("/")
def index():
    return {"message":"Ola k ase"}