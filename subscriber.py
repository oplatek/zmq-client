import zmq

ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)

host = raw_input('Please enter the address (IP or domain name) of the target host: ')
port = raw_input('Please enter the port number: ')

try:
    int(port)
except:
    raise ValueError('The port must be a valid integer.')

print 'Connecting to host...'
socket.connect('tcp://%(host)s:%(port)s' % locals())
print 'Connected successfully.\n'

socket.setsockopt_string(zmq.SUBSCRIBE, '5'.decode('ascii'))

while True:
    value = socket.recv_string()
    print 'Value published: %(value)s' % locals()
