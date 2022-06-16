import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# import zmq
# import struct

class Touches(BaseModel):
    touches: list

output = []

# FASTAPI

app = FastAPI(title='Navi', description='Fingertip Direction MVP Backend')
app.add_middleware(CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],)

# not using whitelists currently. but in case it's necessary:
origins = [ # use 'ipconfig' to detect local ipv4 address
            "https://192.168.0.24:3000", # macbong
            "https://192.168.0.26:3000" # ??? why is 26 necessary???
            "https://192.168.0.28:3000", # g14
            # using DHCP so they may change.

            "https://192.168.0.*:3000", # does wildcard work? doesn't seem like it.
          ]
# NOTE 400 Bad Request error may indicate a whitelist/CORS error.

# RECEIVING - - -

@app.post("/touch")
def receive(touches: Touches): # async 하든가
    # print(touches)
    touches = touches.touches
    # socket.send(b"World")

    global output
    output = touches

# REPORTING - - -

@app.get("/read")
def read():
    global output
    return output


if __name__ == "__main__": 
    uvicorn.run(app, debug=True, port=8000, host='0.0.0.0')


# NOTE Right now, we're using HTTP requests for everything (receiving & reporting touchpoints data).
# This works, but it's slow. Probably, a better solution is to use lightweight messaging libraries like ZeroMQ
# The problem with them has been the blocking behavior, combined with Python's GIL which forces single-threading for all applications.
# It *should* be possible to do this. I just don't know how to do that right now.


# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")


# #  Wait for next request from client
# try: 
#     message = socket.recv()
#     print("Received request: %s" % message)
#     socket.send_json(touches) # maybe: encode before sending.
# except Exception: pass