import network
import time

class WifiConnection:
    def __init__(self, ssid, password, max_retries=10):
        self.ssid = ssid
        self.password = password
        self.max_retries = max_retries
        self.sta_if = network.WLAN(network.STA_IF)

    def connect(self):
        self.disconnect()  # Ensure we start with a clean state
        time.sleep(1)  # Short delay before attempting to connect
        if not self.sta_if.isconnected():
            print('connecting to network...')
            self.sta_if.active(True)
            self.sta_if.connect(self.ssid, self.password)
            for attempt in range(self.max_retries):
                if self.sta_if.isconnected():
                    print('network config:', self.sta_if.ifconfig())
                    return True
                else:  
                    print(f'Attempt {attempt + 1} of {self.max_retries}...')
                    time.sleep(1)
            print('Failed to connect to WiFi after maximum retries.')
            return False
        
    def disconnect(self):
        if self.sta_if.isconnected():
            self.sta_if.disconnect()
            print('Disconnected from WiFi.')    

