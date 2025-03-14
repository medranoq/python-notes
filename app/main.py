import asyncio
import time
from fastapi import FastAPI

app = FastAPI()

def fetch_data() -> list:
    
    data =   [
       {
           "id":1,
           "more_data":{}
       }, {
           "id":2,
           "more_data":{}
       }
    ]
    
    return data

@app.get("/seq-task")
async def seq_task():
    
    print("======= Sequentially task  ========")
    
    print("Fetching API data....")

    time.sleep(3) # Blocking I/O Operation
    
    print("Data fetched")
        
    return {"status":True,"result":"Serving working","data":fetch_data()}



# Run in separte threads

@app.get("/con-task")
async def con_task():
    
    print("======= Concurrently task  ========")
    
    print("Fetching API data....")

    await asyncio.sleep(3) # Non-Blocking I/O Operation
    
    print("Data fetched")
        
    return {"status":True,"result":"Serving working","data":fetch_data()}

@app.get("/par-task")
def par_task():
    
    print("======= Parallely task  ========")
    
    print("Fetching API data....")

    time.sleep(3) # Blocking I/O Operation
    
    print("Data fetched")
        
    return {"status":True,"result":"Serving working","data":fetch_data()}
    