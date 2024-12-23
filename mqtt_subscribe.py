import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttbroker)

# Set the message callback
client.on_message = on_message
# Start the loop and subscribe to the topic
client.loop_start()
client.subscribe("temperature")

# Keep the client active for 30 seconds to receive messages
time.sleep(30)

# Stop the loop and disconnect the client
client.loop_stop()
client.disconnect()
