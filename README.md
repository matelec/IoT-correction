# IoT-picopi-w
---
## Projet IoT BP CIEL 
---
Voici le dépot du firmware des IoTs à base de Raspberry Pico Pi W. Le firmware est codé à la suite du module 6: IoT. 

* `lib`: contient les librairies ssd1306 pour contrôler les écrans Oled et umqtt_simple pour communiquer avec le protocole MQTT.
* `parametres.py`: script python qui charge les paramètres depuis config.json. Il est importé dans main.py.
* `ConnectWifi.py`: librairie permettant de se connecter à un point d'accès wifi. Les paramètres du AP sont dans config.json.
* `Temperature.py`: librairie permettant de lire et calculer la température en °C. Gestion des températures positives ou négatives.
---

Les paramètres sensibles sont enregistrés dans un fichier config.json. Vous devez respecter la structure suivante:

```json
{
  "wifi_ssid": "le ssid",
  "wifi_password": "la clé",
  "mqtt_broker": "l'adresse IP",
  "mqtt_topic": "le topic",
  "mqtt_user": "le compte user",
  "mqtt_password": "mon_mdp"
}




