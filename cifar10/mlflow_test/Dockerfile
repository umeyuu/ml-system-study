FROM ubuntu:20.04

RUN apt-get update \
    && apt-get -yq dist-upgrade \
    && apt-get install -yq \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*