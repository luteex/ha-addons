ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3

WORKDIR /usr/src/app
COPY tcp_server.py /usr/src/app/

COPY rootfs/ /

RUN chmod +x /etc/services.d/tcp_server/run
