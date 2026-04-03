from machine import Pin, SoftI2C
import time


class LectureTemperature:
    def __init__(self, i2c, address=0x48):
        self.i2c = i2c
        self.address = address

    def reset_i2c(self):
        try:
            self.i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=100000, timeout=5000)
            print("I2C bus reset successfully.")
        except Exception as e:
            print("Error resetting I2C bus:", e)

    def lire_temperature(self):
        try:
            # Lire les données de température (2 octets)
            mesure = self.i2c.readfrom_mem(self.address, 0x00, 2)
            # Convertir les données en température (en degrés Celsius)
            val = (mesure[0] << 3)|(mesure[1] >> 5) #reduction de 16 à 11bits.
            if (val > 1023):                        #si valeur négative
                res =  (val ^ 0b11111111111)+1
                self.temperature = - round(res * 0.125, 2)
            else :                                  #si valeur positive              
                self.temperature = round(val * 0.125, 2)
            return self.temperature
        except Exception as e:
            print("Erreur lors de la lecture de la température:", e)
            self.reset_i2c()
            return None
        
