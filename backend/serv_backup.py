import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

global output
output = 'abc'

# FASTAPI

app = FastAPI(title='Navi', description='Fingertip Direction MVP Backend')
origins = ["http://localhost:3000", "https://localhost:3000", "http://192.168.0.169:3000", "https://"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

# RECEIVING

class Touches(BaseModel):
    touches: list

@app.post("/touch")
def receive(touches: Touches): # async 하든가
    global output
    output = touches.touches

    print(type(touches))
    # touches = touches.touches
    # TODO: number the touches to represent finger
    return # return!


if __name__ == "__main__": 
    # uvicorn.run(app, port=8080, host='0.0.0.0')
    uvicorn.run(app, debug=True, port=8000, host='0.0.0.0')


# DEBUG: POST Request
# class Test(BaseModel):
#     test: int
# @app.post("/test")
# def receive(test: Test):
#     print(test.test)
#     return