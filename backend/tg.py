# import cv2
# import numpy as np

# # rr, cc = draw.circle_perimeter(pos[0], pos[1], radius=10, shape=img.shape)
# img = np.zeros(shape=[800,800,3])
# cv2.imshow('touch points viz', img)

# # waits for user to press any key
# # (this is necessary to prevent Python kernel from crashing)
# cv2.waitKey(0)
  
# # closing all open windows
# cv2.destroyAllWindows()

# - - - - - - - - - - - - -

#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import time

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv_json()
    print("Received reply %s [ %s ]" % (request, message))