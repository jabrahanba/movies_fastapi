from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv('config.env')
user = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")


app = FastAPI()

#http://127.0.0.1:8000 ruta raiz local

@app.get("/")
def index():
    return {"message":"Ola k ase"}

@app.get("/consulta1/{mes}")
def index(mes: str):
    client = MongoClient(f'mongodb+srv://{user}:{password}@movies.sytutqr.mongodb.net/')
    db = client["MLOPS"]
    collection = db["movies"]

    meses = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12
    }

    nombre_mes = mes.lower()
    if nombre_mes not in meses:
        print("Nombre de mes inválido.")
    else:
        numero_mes = meses[nombre_mes]
        mes_formateado = str(numero_mes).zfill(2)
        query = {
            "release_date": {
                "$regex": fr"-{mes_formateado}-[0-9]{{2}}"
            }
        }
        count = collection.count_documents(query)
        print(f"Número de documentos encontrados para el mes {nombre_mes.capitalize()}: {count}")
        client.close()
    return {f"consulta para {nombre_mes.capitalize()}":{count}}