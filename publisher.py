import random
import time
import zmq

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind('tcp://*:1235')

while True:
    value = random.randrange(1, 10)
    print 'Sending: %(value)d' % locals()
    socket.send_string(str(value))
    time.sleep(0.5)
