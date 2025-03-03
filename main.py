import json
from ConnectWifi import WiFiConnection
from parametres import SSID, PASSWORD
from Temperature import LectureTemperature
from Affichage import AffichageOled
from machine import Pin, SoftI2C
import ssd1306
import time   


i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)
buttonPin = Pin(19, Pin.IN)
temp=25
wifi = WiFiConnection(ssid=SSID, key=PASSWORD, max_retries=10)    #instance de la classe WifiConnection
capteur_temp = LectureTemperature(i2c,Pin(21),Pin(20))                  #instance de la classe LectureTemperature
ecran = AffichageOled(128, 64, i2c)                     #instance de la classe AffichageOled

# définition de la fonction interruption bouton
def interrupt_button(pin):
    global temp
    ecran.oledTemp(temp)

buttonPin.irq(trigger=Pin.IRQ_RISING, handler=interrupt_button)

# définition du programme principal
def main():
    global temp
   
    ####connection au wifi#####
    print("Connexion au réseau Wi-Fi...")
    wlan = wifi.connect()                                     #connexion au réseau
    if wlan.isconnected():
        print("Connecté avec succès!")
        print("Adresse IP: ", wlan.ifconfig())                  #wlan est utilisable pour d'autres fonctions réseau
    else:
        print("Échec de la connexion.")

    while True:
        temp = capteur_temp.readTemp()
        if temp is not None:
            print(f"Température : {temp} °C")
        time.sleep(5)      

# programme principal.
if __name__ == "__main__":
    main()