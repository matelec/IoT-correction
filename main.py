# appel des librairies
from Temperature import LectureTemperature
from lib import ssd1306
import parametres
from machine import Pin, SoftI2C
from DelRGB import RGB
from ConnectWifi import WifiConnection
from Affichage import AffichageOled
import time

temp=0
maintenant = derniere_lecture = time.ticks_ms()
affichage_actif = False

led=RGB(2,3,4)

print("boot")
led.boot()

# phase d'initialisation
led.init()
i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)
try:
    i2c.scan()
    print("I2C devices found:", i2c.scan())
    if len(i2c.scan()) == 2:
        print("I2C devices detected successfully.")
        led.on('green')
        led.off()
        time.sleep(1)
        led.on('magenta')
    else:
        print("Error: Expected 2 I2C devices, but found", len(i2c.scan()))
        led.erreur()    
except Exception as e:
    print("Error scanning I2C devices:", e)
    led.erreur()
oled=AffichageOled(128, 64, i2c)
time.sleep(1)
wifi=WifiConnection(ssid=parametres.SSID, password=parametres.PASSWORD)
capteur_temp=LectureTemperature(i2c)
bouton = Pin(19, Pin.IN)




# définition de la fonction interruption bouton
def interrupt_button():
    global affichage_actif

    affichage_actif = True


# définition du bouton en interruption
bouton.irq(trigger=Pin.IRQ_FALLING, handler=lambda pin: interrupt_button(Pin))


# définition du programme principal
def main():
    global affichage_actif, temp, maintenant, derniere_lecture

    # appel de la fonction connection au wifi
    led.wifi()
    time.sleep(1)
    if wifi.connect():
        print("Connected to WiFi successfully.")
        led.success()
        oled.afficher_message(wifi.ssid, wifi.sta_if.ifconfig()[0])
        time.sleep(10)  # Affiche le message de connexion pendant 20 secondes
        oled.eteindre()
    else:
        print("Failed to connect to WiFi.")
        led.erreur()
    
    derniere_lecture = time.ticks_ms()
    
    while True:
        maintenant = time.ticks_ms()

        # Mise à jour toutes les 2 minutes
        if time.ticks_diff(maintenant, derniere_lecture) >= 120_000:
            temp = capteur_temp.lire_temperature()
            print("Temperature:", temp, "°C")
            derniere_lecture = maintenant

        # Gestion de l'affichage déclenchée par l'IRQ
        if affichage_actif:
            temp = capteur_temp.lire_temperature()
            time.sleep(1)  # Petite pause pour assurer une lecture stable de la température
            oled.afficher_temperature(temp)
            time.sleep(15)  # Affiche la température pendant 15 secondes
            oled.eteindre()
            affichage_actif = False

        time.sleep(1)  # Petite pause pour éviter une boucle trop rapide

# programme principal.
if __name__ == "__main__":
    main()
