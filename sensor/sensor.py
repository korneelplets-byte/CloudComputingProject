import os
import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "mosquitto")
PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC = os.getenv("MQTT_TOPIC", "sensors/ruimte1")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

while True:
    # Genereer random sensorwaarden
    randominterval = random.randint(1,10)
    if randominterval == 8:
        payload = {
                "temperatuur": round(random.uniform(18.0, 100.0), 1),
                "luchtvochtigheid": round(random.uniform(35.0, 200.0), 1),
                "co2": random.randint(400, 2000)
            }
    else:
        payload = {
            "temperatuur": round(random.uniform(18.0, 26.0), 1),
            "luchtvochtigheid": round(random.uniform(35.0, 75.0), 1),
            "co2": random.randint(400, 1200)
        }
    bericht = json.dumps(payload)

    try:
        client.connect(BROKER, PORT, keepalive=60)
        client.publish(TOPIC, bericht)
        client.disconnect()
        print(f"Verzonden naar '{TOPIC}': {bericht}")
    except Exception as e:
        print(f"Wachten op MQTT broker ({BROKER}:{PORT})... Fout: {e}")

    time.sleep(5)