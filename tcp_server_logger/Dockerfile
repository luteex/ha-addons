ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3

WORKDIR /usr/src/app

# Zkopíruj Python server do pracovního adresáře
COPY tcp_server.py /usr/src/app/

# Zkopíruj rootfs (obsahuje run.sh)
COPY rootfs/ /

# Ujisti se, že startovací skript je spustitelný
RUN chmod a+x /run.sh

# Spouštěcí příkaz
CMD [ "/run.sh" ]
