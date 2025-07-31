FROM python:slim
RUN pip install paho-mqtt
COPY sensor.py /sensor.py
ENTRYPOINT ["python", "/sensor.py"]