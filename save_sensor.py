import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)

    # save temperature
    with open("temp.csv", "a") as f:
        f.write(str(data["temperature"]) + "\n")

    # save humidity
    with open("hum.csv", "a") as f:
        f.write(str(data["humidity"]) + "\n")

    # save soil moisture
    with open("shum.csv", "a") as f:
        f.write(str(data["soil_moisture"]) + "\n")

    # save light
    with open("lum.csv", "a") as f:
        f.write(str(data["light"]) + "\n")


client = mqtt.Client()
client.connect("localhost", 1883)

client.subscribe("greenhouse/sensors")
client.on_message = on_message

client.loop_forever()