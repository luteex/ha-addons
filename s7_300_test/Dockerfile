FROM python:3.11-alpine

RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers

RUN pip install python-snap7

COPY run.sh /run.sh
COPY test.py /test.py

RUN chmod +x /run.sh

CMD ["/run.sh"]
