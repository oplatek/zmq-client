import zmq

ctx = zmq.Context()
socket = ctx.socket(zmq.REQ)

host = raw_input('Please enter the address (IP or domain name) of the target host: ')
port = raw_input('Please enter the port number: ')

try:
    int(port)
except:
    raise ValueError('The port must be a valid integer.')

print 'Attempting to connect...'
socket.connect('tcp://%(host)s:%(port)s' % locals())
print 'Connected successfully. You may type messages and press `Enter` to send.'

while True:
    message = raw_input('> ')
    socket.send(message)
    response = socket.recv()
    print 'Server replied with:'
    print '%(response)s' % locals()
