FROM python:3.12-slim

RUN groupadd -g 10000 python_runer && \ 
    useradd python_runer -u 10000 -g python_runer -s /bin/bash -m && \
    echo '%python_runer ALL=(ALL:ALL) NOPASSWD: ALL'


USER python_runer
WORKDIR /home/python_runer
COPY app/server.py .
CMD [ "python3", "server.py" ]

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl http://localhost:8080/health" ]