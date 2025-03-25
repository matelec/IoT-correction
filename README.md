# IoT-picopi-w
---
## Projet IoT BP CIEL 
---
Voici le dépot du firmware des IoTs à base de Raspberry Pico Pi W. Le firmware est codé à la suite du module 6: IoT. 

* `lib`: contient la librairie ssd1306 pour contrôler les écrans Oled.
* `parametres.py`: script python qui charge les paramètres depuis config.json. Il est importé dans main.py.
* `ConnectWifi.py`: librairie permettant de se connecter à un point d'accès wifi. Les paramètres du AP sont dans config.json.
* `Temperature.py`: librairie permettant de lire et calculer la température en °C. Gestion des températures positives ou négatives.
* `main.py`: script du programme principal. Le code respecte la structure du document lancement partie 2.pdf sur le site moodle-bpciel.mratte.ovh.
* `DelRGB.py`: librairie permettant de piloter la DEL RVB afin de donner des informations visuelles sur le focntionnement avec les couleurs.
---

Les paramètres sensibles sont enregistrés dans un fichier config.json. Vous devez respecter la structure suivante:

```json
{
  "wifi_ssid": "le ssid",
  "wifi_password": "la clé",
}




