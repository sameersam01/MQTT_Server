import paho.mqtt.client as mqtt
from random import randrange,uniform
import time

mqttbroker="mqtt.eclipseprojects.io"
client=mqtt.Client("Temperature_inside")
client.connect(mqttbroker)

while True:
    randomNumber=uniform(20.0,21.0)
    client.publish("temperature",randomNumber)
    print("Just published" + str(randomNumber)+ "to the topic Temperature")
    time.sleep(1)


