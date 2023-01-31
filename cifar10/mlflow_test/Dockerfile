FROM ubuntu:20.04

RUN apt-get update \
    && apt-get -yq dist-upgrade \
    && apt-get install -yq \
    wget \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --user pandas