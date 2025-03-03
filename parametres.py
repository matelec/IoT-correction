import json
import ubinascii
import machine

# Charger le fichier JSON
try:
    with open("config.json", "r") as file:
        config = json.load(file)
except Exception as e:
    print("❌ Erreur : Impossible de charger config.json !", e)
    config = {}  # Evite une erreur fatale si le fichier est absent

# Wi-Fi
SSID = config.get("wifi_ssid", "default_ssid")
PASSWORD = config.get("wifi_password", "default_password")

# MQTT
MQTT_BROKER = config.get("mqtt_broker", "default_broker")
MQTT_TOPIC = config.get("mqtt_topic", "default_topic")
MQTT_USER = config.get("mqtt_user", "default_user")
MQTT_PASSWORD = config.get("mqtt_password", "default_password")

# Identifiant unique pour le client MQTT
MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()

print(f"📡 Paramètres chargés : WiFi={SSID}, Broker={MQTT_BROKER}")