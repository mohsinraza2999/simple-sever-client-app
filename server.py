from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Data(BaseModel):
    message: str
fruits:dict={"dasi":["apricot","cherry","apple"],"other":["banana","watemelon"]}

@app.get("/")
def read_root():
    return {"message": "Hello from server"}

def userwant(key):
    try:
        return fruits[key]
    except:
        return "no data related to the query!"

@app.post("/send/")
def receive_data(data: Data):
    userchoice=userwant(data.message)
    return {"received": userchoice}
#if __name__=="__main__":
#    uvicorn.run(app=app,host='0.0.0.0',port=8000)
