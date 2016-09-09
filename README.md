# Requirements
* Docker

# Installation
Run `docker build -t zmq_client .` from the root of the repository to build
the docker image and name it "zmq_client".

# Usage
Run `docker run -ti zmq_client` and then follow the prompts.

## Note
The target host must have ZMQ listening on the specified port, with the REP connection type.
An example of such an implementation can be seen in `server.py`.
The `client.py` file contains the code for the program run by the Docker container.
