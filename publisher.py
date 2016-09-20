import random
import time
import zmq

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind('tcp://*:1235')

while True:
    value = random.randrange(0, 1)
    socket.send_string('%i' % value)
    time.sleep(0.5)