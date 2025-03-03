import ssd1306
import time

class AffichageOled:
    def __init__(self, width, height, i2c):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.oled = ssd1306.SSD1306_I2C(width, height, i2c)

    def oledTemp(self,temperature):
        self.oled.fill(0)
        self.oled.fill_rect(0, 0, 32, 32, 1)
        self.oled.fill_rect(2, 2, 28, 28, 0)
        self.oled.vline(9, 8, 22, 1)
        self.oled.vline(16, 2, 22, 1)
        self.oled.vline(23, 8, 22, 1)
        self.oled.fill_rect(26, 24, 2, 4, 1)
        self.oled.text('TEMPERATURE', 40, 0)
        self.oled.text(str(temperature), 40, 20)
        self.oled.pixel(91, 20,1)
        self.oled.pixel(90, 21,1)
        self.oled.pixel(90, 22,1)
        self.oled.pixel(91, 23,1)
        self.oled.pixel(92, 21,1)
        self.oled.pixel(92, 22,1)
        self.oled.text('C', 96, 20)
        self.oled.show()
        time.sleep(5)
        self.oled.fill(0)
        self.oled.show()
