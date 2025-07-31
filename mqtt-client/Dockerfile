FROM python:slim
RUN pip install paho-mqtt
COPY sensor.py /sensor.py
CMD ["python", "/sensor.py"]