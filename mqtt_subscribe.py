import paho.mqtt.client as mqtt
import time

# Define the message callback
def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")

try:
    client.connect(mqttbroker)
    print(f"Connected to MQTT broker at {mqttbroker}")
    
    # Set the message callback
    client.on_message = on_message
    
    # Start the loop and subscribe to the topic
    client.loop_start()
    client.subscribe("temperature")
    print("Subscribed to topic 'temperature'")
    
    # Keep the client active for 30 seconds to receive messages
    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")


