import time
import random
import paho.mqtt.client as mqtt
import signal
import sys
import os

# Global run flag
running = True


def get_required_env(var_name):
    """Get required environment variable or exit with error if not found."""
    value = os.getenv(var_name)
    if value is None:
        print(
            f"ERROR: Required environment variable '{var_name}' is not set",
            file=sys.stderr,
        )
        sys.exit(1)
    return value


# MQTT configuration from environment variables (required)
MQTT_BROKER_HOST = get_required_env("MQTT_BROKER_HOST")
MQTT_BROKER_PORT = int(get_required_env("MQTT_BROKER_PORT"))
MQTT_TOPIC = get_required_env("MQTT_TOPIC")


# Helper function to handle graceful shutdown
def handle_stop(_signum, _frame):
    global running
    running = False


signal.signal(signal.SIGTERM, handle_stop)
signal.signal(signal.SIGINT, handle_stop)

# Connect to the MQTT broker
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

while running:
    # Use a Gaussian distribution for the temperature values
    temp = random.gauss(20, 5)
    # Assemble the MQTT message in InfluxDB line protocol
    payload = f"temperature,location=virtual value={temp:.2f}"
    # Show the MQTT message on the console
    print(payload, flush=True)
    # Publish the MQTT message to the broker
    client.publish(MQTT_TOPIC, payload)
    # Avoid blocking for too long
    for _ in range(10):
        if not running:
            break
        time.sleep(1)

# Cleanup on shutdown
client.disconnect()
sys.exit(0)
