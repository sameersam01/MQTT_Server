import paho.mqtt.client as mqtt
import time

def on_message(client,userdata,message):
    print("Received message: ",str(message.payload.decode("utf-8")))

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttbroker)

client.loop_start()
client.subscribe("Temperature")
client._on_message=on_message


time.sleep(3)
client.loop_stop()