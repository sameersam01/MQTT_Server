import paho.mqtt.client as mqtt
from random import uniform
import time

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_inside")
client.connect(mqttbroker)

try:
    while True:
        randomNumber = uniform(20.0, 21.0)
        client.publish("temperature", randomNumber)
        print("Just published " + str(randomNumber) + " to the topic temperature")
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnecting from broker...")
    client.disconnect()
    print("Disconnected successfully.")
