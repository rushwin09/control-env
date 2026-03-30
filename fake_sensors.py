import paho.mqtt.client as mqtt
import time
import random

# Configuration matching the ESP32 and Node-RED settings
BROKER = "127.0.0.1" 
TOPICS = {
    "temperature": "tempg",
    "humidity": "humg",
    "soil_humidity": "shumg",
    "light": "luxg"
}

client = mqtt.Client()

try:
    client.connect(BROKER, 1883)
    print(f"Connected to {BROKER}. Simulating ESP32 sensor data...")
except Exception as e:
    print(f"Connection failed: {e}. Ensure WSL has internet access.")
    exit(1)

try:
    while True:
        # Generate realistic greenhouse readings
        temp = round(random.uniform(22.0, 30.0), 2)
        hum = round(random.uniform(45.0, 65.0), 2)
        soil = round(random.uniform(30.0, 80.0), 2)
        lux = random.randint(1000, 3500)

        # Publish individual values to the topics defined in the project
        client.publish(TOPICS["temperature"], temp)
        client.publish(TOPICS["humidity"], hum)
        client.publish(TOPICS["soil_humidity"], soil)
        client.publish(TOPICS["light"], lux)
        
        # Signal that the "device" is online
        client.publish("ESPstatus", "on")

        print(f"Published -> Temp: {temp}C, Hum: {hum}%, Soil: {soil}%, Light: {lux}")
        time.sleep(10) 
except KeyboardInterrupt:
    print("\nSimulation stopped.")
    client.disconnect()