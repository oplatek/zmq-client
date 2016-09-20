import zmq

ctx = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:1234')

while True:
    message = socket.recv()
    socket.send(b'Received. Message was: "%(message)s"' % locals())
