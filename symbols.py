import paho.mqtt.client as mqtt
import time

# Broker settings
broker_address = "mqtt-dashboard.com"  # Replace with your broker
port = 1883  # Default MQTT port

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, port)

# Keep connection alive
client.loop_start()

# Define the topic
topic = "test/symbols"

# Define messages (symbols) you want to send
symbols = ["❤️", "🚀", "🔥", "💡", "🎉", "💻", "🎯", "🔔", "🚴"]

# Function to publish messages asynchronously
def publish_messages():
    for symbol in symbols:
        # Publish message with QoS 0 for maximum speed
        client.publish(topic, symbol, qos=0)
        print(f"Sent symbol: {symbol}")

# Accelerated batch publish
publish_messages()

# Allow some time to ensure all messages are sent before disconnecting
time.sleep(1)

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()

print("All symbols sent.")
