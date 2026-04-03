import ssd1306
import time

class AffichageOled:
    def __init__(self, width, height, i2c):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.oled = ssd1306.SSD1306_I2C(self.width, self.height, self.i2c)

    def eteindre(self):
        self.oled.fill(0)
        self.oled.show()

    def afficher_temperature(self, message):
        self.oled.fill(0)  # Efface l'écran
        self.oled.rect(0, 0, self.width, self.height,1)  # Dessine un double rectangle autour du message
        self.oled.rect(2, 2, self.width-4, self.height-4, 1) 
        self.oled.text("TEMPERATURE:", 10, 20)  # Affiche le titre à la position (10, 20)
        self.oled.text(str(message), 40, 30)  # Affiche le message à la position (40, 30)
        # affichage du round pour degré celcius
        for i in range(3):
            for j in range(3):
                self.oled.pixel(81+i, 30+j, 1)  
        self.oled.text('C', 86, 30) 
        self.oled.show()  # Met à jour l'affichage

    def afficher_message(self,ssid,ipconfig):
        self.oled.fill(0)  # Efface l'écran
        self.oled.text("Connected : ", 10, 20)  # Affiche le titre à la position (10, 20)
        self.oled.text(ssid, 10, 30)  # Affiche le SSID à la position (10, 30)
        self.oled.text(ipconfig, 10, 40)  # Affiche la configuration IP à la position (10, 40)
        self.oled.show()  # Met à jour l'affichage
        time.sleep(15)  # Affiche le message pendant 15 secondes