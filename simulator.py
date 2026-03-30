import paho.mqtt.client as mqtt
import time
import random

# Configuration - matching the ESP32 settings
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
# Topics used by Node-RED and ESP32
TOPICS = {
    "temperature": "tempg",
    "humidity": "humg",
    "soil_humidity": "shumg",
    "light": "luxg"
}

client = mqtt.Client()

def simulate_sensors():
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print(f"Connected to {MQTT_BROKER}. Sending fake data...")
        
        while True:
            # Generate fake values based on ESP32 logic
            temp = round(random.uniform(20.0, 35.0), 2)
            hum = round(random.uniform(40.0, 70.0), 2)
            shum = round(random.uniform(30.0, 80.0), 2)
            lux = random.randint(500, 4000)

            # Publish data to the same topics the ESP32 uses
            client.publish(TOPICS["temperature"], str(temp))
            client.publish(TOPICS["humidity"], str(hum))
            client.publish(TOPICS["soil_humidity"], str(shum))
            client.publish(TOPICS["light"], str(lux))
            client.publish("ESPstatus", "on") # Tell Node-RED the "ESP" is online

            print(f"Sent: Temp={temp}, Hum={hum}, Soil={shum}, Lux={lux}")
            time.sleep(5) # Matches the ESP32 send interval
            
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    simulate_sensors()