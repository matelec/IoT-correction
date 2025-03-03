import network
import time

class WiFiConnection:
    def __init__(self, ssid, key, max_retries=10):
        self.ssid = ssid
        self.key = key
        self.max_retries = max_retries
        self.sta_if = network.WLAN(network.STA_IF)

    def connect(self):
        if not self.sta_if.isconnected():
            print('Connecting to network...')
            self.sta_if.active(True)
            self.sta_if.connect(self.ssid, self.key)
            
            retries = 0
            while not self.sta_if.isconnected() and retries < self.max_retries:
                time.sleep(1)
                retries += 1
                print(f'Retrying... {retries}/{self.max_retries}')
            
            if not self.sta_if.isconnected():
                print("Failed to connect to the network.")
                return None
        
        print('Network config:', self.sta_if.ifconfig())
        return self.sta_if

    def disconnect(self):
        if self.sta_if.isconnected():
            self.sta_if.disconnect()
            print('Disconnected from the network.')
