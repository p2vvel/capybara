FROM ubuntu:22.04


RUN apt-get update && apt-get install -y \
    wget


RUN wget 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' -O /tmp/code.tar.gz && \
    tar -xvzf /tmp/code.tar.gz && \
    mv code /usr/local/bin/code && \
    rm /tmp/code.tar.gz


RUN mkdir /workspace
WORKDIR /workspace


ENTRYPOINT ["code", "tunnel", "--random-name", "--accept-server-license-terms"]