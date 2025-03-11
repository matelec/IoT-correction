import time
from machine import Pin, SoftI2C

class LectureTemperature:
    def __init__(self, i2c, scl, sda):
          self.i2c = i2c
          self.scl = scl
          self.sda = sda
          self.temperature = None
          
    def reset_i2c(self):
        """ Réinitialise le bus I2C en cas d'erreur """
        print("⚠️ Réinitialisation du bus I2C...")
        self.i2c= SoftI2C(scl=self.scl, sda=self.sda, freq=100000, timeout=5000)
        time.sleep(0.1)    

    def readTemp(self):
#        buf = bytearray(1)  # création d’un buffer 1 octet
#        buf[0] = 0x00  # adresse du registre point
#        print("avant écriture")
#        self.i2c.writeto(0x48, buf)  # écriture dans le LM75
#        print("avant lecture")
        try:
            mesure = self.i2c.readfrom_mem(0x48, 0x00, 2)  # lecture
#        	print(mesure)
            val = (mesure[0] << 3)|(mesure[1] >> 5) #reduction de 16 à 11bits.
            if (val > 1023):                        #si valeur négative
                res =  (val ^ 0b11111111111)+1
                self.temperature = - res * 0.125
            else :                                  #si valeur positive              
                self.temperature = val * 0.125
            print("temperature:",self.temperature)
            return self.temperature
        except OSError as e:
            print(f"Erreur I2C : {e}")
            self.reset_i2c()  # Réinitialiser le bus
            return None