FROM python:slim@sha256:08a4c22c92b79ec821a7ad49768480039ee5b7accac3955228e75366e30abc8e
RUN pip install paho-mqtt
COPY sensor.py /sensor.py
ENTRYPOINT ["python", "/sensor.py"]