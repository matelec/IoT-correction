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

print(f"📡 Paramètres chargés : WiFi={SSID}")