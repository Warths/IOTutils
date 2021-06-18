from network import WLAN, STA_IF
from time import sleep

class STA:
    def __init__(self, SSID, PASS, timeout):
        """
        WIFI Station
        :param str SSID: Access point Name
        :param str PASS: Access point Password
        :param int timeout: seconds before aborting connexion 
        """

        self.SSID = SSID
        self.PASS = PASS
        self.IF = WLAN(STA_IF)
        
        self.timeout = timeout
        
    def connect(self):
        """
        Connect to the Wifi Access Point.
        :raise: OSError if connection fails
        """
        self.IF.active(True)
        self.IF.connect(self.SSID, self.PASS)
        self.wait_for_connection(self.IF, self.timeout)
        
    def disconnect(self):
        """
        Disconnect from the Wifi Access Point.
        """
        self.IF.disconnect()
        self.IF.active(False)
        
    def wait_for_connection(self):
        """
        Wait for the Interface to be connected to the Access Point
        :raise: OSError if connection fails
        """
        seconds_elapsed = 0
        while not self.IF.isconnected():
            if seconds_elapsed >= self.timeout:
                self.IF.active(False)
                raise OSError
            sleep(1) 
            seconds_elapsed += 1
            
