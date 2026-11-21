FROM python:slim@sha256:65a65fc7b30b06cb6df4930fd4650697cb23f4c2698ab81fc87e4b031bc36928
RUN pip install paho-mqtt
COPY sensor.py /sensor.py
ENTRYPOINT ["python", "/sensor.py"]