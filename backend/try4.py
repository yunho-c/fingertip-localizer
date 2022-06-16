from skimage import draw
import numpy as np
import cv2
import time
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pygame

# BLOCK (GLOBAL)
block = False

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
    touches = touches.touches
    visualize(touches)
    # TODO: number the touches to represent finger
    return # return!


# FEATURES

# align fingers
def identify(touches):
    # description: 
    # get a list of indices, sorted based on x coordinate
    # create and return a new list    
    # for i, touch in enumerate(touches):

    return # sorted (from thumb, index, middle, ring, little) list of fingertip locations


def draw_finger(img, pos, type=None):
    img = img.copy()
    rr, cc = draw.circle_perimeter(pos[0], pos[1], radius=10, shape=img.shape)
    img[rr, cc] = [255,0,0]
    return img


def visualize(touches): 
    global block
    if block: return
    block = True

    img = np.zeros(shape=[800,800,3])
    print(img.shape)
    for touch in touches:
        # print(touch)
        # img = draw_finger(img, [int(n) for n in touch])
        img = draw_finger(img, touch)
    # print(img)
    print(img.shape)

    cv2.imshow('touch points viz', img)
    cv2.waitKey(0)

    block = False


# # closing all open windows


# OPTIMIZATION
# reference Navi for real-time processing details.
# flow control probably required.
# output is Arduino commands — serial outputs, most likely.


def send_commands(): pass

def gaze(): pass

def sight():
    return cv2.imread('.jpg')

# while True:
#     time.sleep(1)
#     # time.sleep(0.015)
#     try:
#         print(serv_backup.output)
#     except Exception: pass


if __name__ == "__main__": 
    # uvicorn.run(app, port=8080, host='0.0.0.0')
    uvicorn.run(app, debug=True, port=8000, host='0.0.0.0')
    cv2.destroyAllWindows()


# DEBUG: POST Request
# class Test(BaseModel):
#     test: int
# @app.post("/test")
# def receive(test: Test):
#     print(test.test)
#     return