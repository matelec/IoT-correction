# 🌡️ Thermomètre connecté – MicroPython

Projet embarqué sur microcontrôleur (type RP2040 / ESP32) permettant de lire la température via un capteur I²C, de l'afficher sur un écran OLED SSD1306, et de se connecter au Wi-Fi. L'affichage est déclenché par appui sur un bouton physique.

---

## 📋 Fonctionnalités

- Lecture de la température toutes les **2 minutes** via un capteur I²C (TMP1xx, adresse `0x48`)
- Affichage sur écran **OLED 128×64** (SSD1306) à la demande (bouton poussoir)
- Connexion **Wi-Fi** au démarrage avec affichage de l'adresse IP
- **LED RGB** comme indicateur d'état (boot, init, Wi-Fi, MQTT, succès, erreur)
- Gestion des **interruptions** matérielles pour le bouton

---

## 🗂️ Structure du projet

```
├── main.py              # Programme principal
├── parametres.py        # Chargement de la configuration depuis config.json
├── config.json          # Fichier de configuration (non versionné)
├── Temperature.py       # Classe de lecture du capteur de température I²C
├── Affichage.py         # Classe de gestion de l'écran OLED
├── ConnectWifi.py       # Classe de connexion Wi-Fi
├── DelRGB.py            # Classe de contrôle de la LED RGB
└── lib/
    └── ssd1306.py       # Driver MicroPython pour l'écran SSD1306
```

---

## ⚙️ Configuration

Créer un fichier `config.json` à la racine du projet avec le contenu suivant :

```json
{
  "wifi_ssid": "nom_de_votre_reseau",
  "wifi_password": "votre_mot_de_passe"
}
```

> ⚠️ Ce fichier contient des informations sensibles. Ne le versionnez pas (ajoutez-le à `.gitignore`).

---

## 🔌 Câblage

| Composant         | Broche microcontrôleur |
|-------------------|------------------------|
| I²C SCL           | GPIO 21                |
| I²C SDA           | GPIO 20                |
| LED RGB – Rouge   | GPIO 2                 |
| LED RGB – Vert    | GPIO 3                 |
| LED RGB – Bleu    | GPIO 4                 |
| Bouton poussoir   | GPIO 19                |

> Le bus I²C est partagé entre le capteur de température (adresse `0x48`) et l'écran OLED (adresse `0x3C`). Le programme vérifie la présence des **2 périphériques** au démarrage.

---

## 💡 Indicateurs LED RGB

| Couleur   | Signification              |
|-----------|----------------------------|
| 🟡 Jaune  | Boot en cours              |
| 🟣 Magenta| Initialisation             |
| 🔵 Cyan   | Tentative de connexion Wi-Fi|
| 🟢 Vert   | Succès / Opération réussie |
| 🔵 Bleu   | Connexion MQTT             |
| 🔴 Rouge  | Erreur (clignotant)        |

---

## 🚀 Démarrage

1. Copier tous les fichiers sur le microcontrôleur (via Thonny, rshell, ou mpremote)
2. Créer le fichier `config.json` avec vos identifiants Wi-Fi
3. Réinitialiser le microcontrôleur — `main.py` s'exécute automatiquement

Au démarrage, le programme :
1. Vérifie les périphériques I²C
2. Se connecte au Wi-Fi et affiche l'IP sur l'écran pendant 15 secondes
3. Entre en boucle principale : appuyez sur le bouton pour afficher la température pendant 15 secondes

---

## 📦 Dépendances

- [MicroPython](https://micropython.org/) (v1.20+)
- Driver `ssd1306.py` inclus dans `lib/` (compatible MicroPython officiel)
- Module `network` (intégré à MicroPython)

---

## 📄 Licence

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.