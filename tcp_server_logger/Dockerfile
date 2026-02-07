ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

COPY tcp_server.py .

CMD ["python3", "tcp_server.py"]
