FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-dev \
        python3-pip \        
        libpq-dev
