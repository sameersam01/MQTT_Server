import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received message:", str(message.payload.decode("utf-8")))

mqttbroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttbroker)

client.on_message = on_message
client.loop_start()
client.subscribe("device/acceleration")  # Update to match the topic
print("Subscribed to 'device/acceleration' topic.")

# Keep running to display messages
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()
    client.disconnect()
