import paho.mqtt.client as mqtt
from random import uniform,randrange
import time

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_outside")
client.connect(mqttbroker)
n=0
try:
    while n<5:
        randomNumber = randrange(10)
        client.publish("temperature", randomNumber)
        print("Just published " + str(randomNumber) + " to the topic temperature")
        time.sleep(1)
        n=n+1
except KeyboardInterrupt:
    print("Disconnecting from broker...")
    client.disconnect()
    print("Disconnected successfully.")
