import numpy as np
import cv2
from skimage import draw
import pygame
import time

import requests

# FEATURES

def visualize_gaze(sight, gaze):
    pass
    # TODO write this in a separate file (with test).

# align fingers
def identify(touches):
    # description: 
    # get a list of indices, sorted based on x coordinate
    # create and return a new list    
    # for i, touch in enumerate(touches):

    return # sorted (from thumb, index, middle, ring, little) list of fingertip locations


def draw_finger(img, pos, type=None):
    img = img.copy()
    # rr, cc = draw.disk((pos[0], pos[1]), radius=10, shape=img.shape)
    rr, cc = draw.circle_perimeter(pos[0], pos[1], radius=10, shape=img.shape)
    img[rr, cc] = [255,0,0]
    return img

# PYGAME

pygame.init()
pygame.display.set_caption("touch position viz")
surface = pygame.display.set_mode([800,800])

cap = cv2.VideoCapture(0)

def visualize(touches): # flow control is no more necessary, since main loop is used.
    # img = np.zeros(shape=[800,800,3])
    # img = cv2.cvtColor(cv2.imread('./ex_im.jpg'), cv2.COLOR_BGR2RGB)
    _, img = cap.read()
    img = np.rot90(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # may need to np.fliplr()
    # print(img.shape)
    for touch in touches:
        # print(touch)
        # img = draw_finger(img, [int(n) for n in touch])
        img = draw_finger(img, touch)
    # print(img)
    # print(img.shape)

    surface.blit(pygame.surfarray.make_surface(img), (0,0))
    pygame.display.flip()


# # closing all open windows
# cv2.destroyAllWindows()


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

stop = False
while not stop:
    # socket.send(b"_") # to alert server
    # message = socket.recv_json() # receive new touch data from server
    # # note: without touch, server will not respond.
    r = requests.get('http://localhost:8000/read')

    message = r.json()
    # print(message)

    if message is not None: visualize(message)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            stop = True