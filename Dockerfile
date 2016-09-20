FROM ubuntu:trusty
MAINTAINER neal.ormsbee@gmail.com
RUN apt-get -y update
RUN apt-get -y install --fix-missing libtool pkg-config build-essential autoconf automake uuid-dev python python-dev python-pip gcc
RUN mkdir -p /home/ubuntu
ADD zeromq-4.1.5.tar.gz /home/ubuntu
WORKDIR /home/ubuntu/zeromq-4.1.5
RUN ./configure
RUN make
RUN make install
WORKDIR /home/ubuntu
RUN pip install pyzmq
COPY client.py server.py subscriber.py publisher.py /home/ubuntu/
CMD python client.py
