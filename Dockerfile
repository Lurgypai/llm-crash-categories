FROM ubuntu:22.04

WORKDIR /workspace

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    vim \
    curl \
    && apt clean

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN pip install ollama
RUN pip install pydantic

COPY ./docker_contents .
