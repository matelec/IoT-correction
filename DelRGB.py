import time
from machine import Pin

class RGB: 
    def __init__(self, r, g, b):
        self.r = Pin(r, Pin.OUT)
        self.g = Pin(g, Pin.OUT)
        self.b = Pin(b, Pin.OUT)

    def off(self):
        self.r.value(0)
        self.g.value(0)
        self.b.value(0)

    def on(self,color):
        if color == 'red':
            self.r.value(1)
            self.g.value(0)
            self.b.value(0)
        elif color == 'green':
            self.r.value(0)
            self.g.value(1)
            self.b.value(0)
        elif color == 'blue':
            self.r.value(0)
            self.g.value(0)
            self.b.value(1)
        elif color == 'yellow':
            self.r.value(1)
            self.g.value(1)
            self.b.value(0)
        elif color == 'cyan':
            self.r.value(0)
            self.g.value(1)
            self.b.value(1)
        elif color == 'magenta':
            self.r.value(1)
            self.g.value(0)
            self.b.value(1)
        elif color == 'white':
            self.r.value(1)
            self.g.value(1)
            self.b.value(1) 

    def erreur(self):
        while True:
            self.on('red')
            time.sleep(0.5)
            self.off()
            time.sleep(0.5)
            
    def boot(self):
        self.on('yellow')
        time.sleep(1)   

    def init(self):
        self.on('magenta')
        time.sleep(1)

    def success(self):
        for i in range(3):
            self.on('green')
            time.sleep(1)
            self.off()
            time.sleep(1)
            self.on('magenta')
        self.on('green')    

    def wifi(self):
        self.on('cyan')
        time.sleep(1)

    def mqtt(self):
        self.on('blue')
        time.sleep(1)              