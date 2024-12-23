import paho.mqtt.client as mqtt
from random import uniform,randrange
import time

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_outside")
client.connect(mqttbroker)

try:
    while True:
        randomNumber = randrange(10)
        client.publish("temperature", randomNumber)
        print("Just published " + str(randomNumber) + " to the topic temperature")
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnecting from broker...")
    client.disconnect()
    print("Disconnected successfully.")
