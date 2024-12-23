const mqtt = require('mqtt');
const client = mqtt.connect('wss://test.mosquitto.org:8081'); // Use WebSocket for web dashboards

client.on('connect', () => {
    console.log('Connected to MQTT broker');
    client.subscribe('device/acceleration');
});

client.on('message', (topic, message) => {
    console.log(`Received message from ${topic}: ${message.toString()}`);
});
