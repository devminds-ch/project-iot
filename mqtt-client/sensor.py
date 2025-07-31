import time
import random
import paho.mqtt.client as mqtt
import signal
import sys

# Global run flag
running = True
# Helper function to handle graceful shutdown
def handle_stop(signum, frame):
    global running
    running = False

signal.signal(signal.SIGTERM, handle_stop)
signal.signal(signal.SIGINT, handle_stop)

# Connect to the MQTT broker
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("mqtt-broker", 1883, 60)

while running:
    # Use a Gaussian distribution for the temperature values
    temp = random.gauss(20, 5)
    # Assemble the MQTT message in InfluxDB line protocol
    payload = f"temperature,location=virtual value={temp:.2f}"
    # Show the MQTT message on the console
    print(payload, flush=True)
    # Publish the MQTT message to the broker
    client.publish("sensors", payload)
    # Avoid blocking for too long
    for _ in range(10):
        if not running:
            break
        time.sleep(1)

# Cleanup on shutdown
client.disconnect()
sys.exit(0)