FROM alpine:3.19

RUN apk add --no-cache python3

WORKDIR /app

COPY tcp_server.py /app/

CMD ["python3", "-u", "/app/tcp_server.py"]
