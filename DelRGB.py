from machine import Pin
import time

class RGB:
    def __init__(self, pin_r, pin_g, pin_b):
        self.r = Pin(pin_r, Pin.OUT)
        self.g = Pin(pin_g, Pin.OUT)
        self.b = Pin(pin_b, Pin.OUT)
         
         
    def off(self):
        self.r.value(0)
        self.g.value(0)
        self.b.value(0)
    
    def on(self,color):
        if color=='red':
            self.r.value(1)
            self.g.value(0)
            self.b.value(0)
        if color=='green':
            self.r.value(0)
            self.g.value(1)
            self.b.value(0)
        if color=='blue':
            self.r.value(0)
            self.g.value(0)
            self.b.value(1)

    def blink(self,color,delay,number):
        for i in range(number):
            self.on(color)
            time.sleep_ms(delay)
            self.off()
            time.sleep_ms(delay)