from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Data(BaseModel):
    message: str
fruits_db:dict={"desi":["apricot","cherry","apple"],"other":["banana","watemelon"]}

@app.get("/")
def read_root():
    return {"message": "Hello from server"}

#This function accepts a key and returns the corresponding value from the fruit database.
def userwant(key):
    try:
        return fruits_db[key]
    except:
        return "no data related to the query!"

@app.post("/send/")
def receive_data(data: Data):
    userchoice=userwant(data.message)
    return {"received": userchoice}


"""
Entry point for deploying the FastAPI application using Uvicorn.

This script runs the FastAPI `app` instance on host 0.0.0.0 and port 8000,
making it accessible externally. It is intended to be used in production or
containerized environments where the application needs to be reachable from
outside the local machine.

Usage:
    python server.py

Note:
    For advanced deployment (e.g., with Gunicorn), consider using a production-ready ASGI server configuration.
"""
if __name__=="__main__":
    uvicorn.run(app=app,host='0.0.0.0',port=8000)
