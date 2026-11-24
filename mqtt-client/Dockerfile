FROM python:slim@sha256:63bb298d2b7b88f176f51b5189f54ce6535c997682ea70885d2132f5d473a8a5
RUN pip install paho-mqtt
COPY sensor.py /sensor.py
ENTRYPOINT ["python", "/sensor.py"]