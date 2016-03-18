FROM debian:testing
MAINTAINER slawomir.zborowski@hotmail.com

ARG http_proxy
ARG https_proxy
ENV http_proxy=$http_proxy https_proxy=$https_proxy

RUN apt-get update -yqq
RUN apt-get install -yqq build-essential wget xz-utils libssl-dev python3-pip

WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
RUN tar xfJ Python-3.5.1.tar.xz
WORKDIR /tmp/Python-3.5.1
RUN ./configure
RUN make
RUN make install

RUN pip3 install aiohttp
