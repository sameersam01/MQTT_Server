import paho.mqtt.client as mqtt
import time
import random  # Simulating acceleration values for demonstration

mqttbroker = "mqtt.eclipseprojects.io"
topic = "device/acceleration"
client = mqtt.Client("AccelerometerDevice")
client.connect(mqttbroker)

while True:
    # Replace the simulated value with actual acceleration data from your device
    acceleration = random.uniform(0, 10)  # Simulating acceleration in m/s^2
    client.publish(topic, f"Acceleration: {acceleration:.2f} m/s^2")
    print(f"Published: Acceleration: {acceleration:.2f} m/s^2")
    time.sleep(1)
