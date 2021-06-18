from . import STA, AP

class WifiStation:
    def __init__(self, sta_ssid, sta_pass, ap_ssid, ap_pass, timeout=10):
        """
        Basic Wifi Station handling both Station and Access point WLAN mode
        
        :param str sta_ssid: SSID of the targeted Access Point 
        :param str sta_pass: Password of the targeted Access Point
        :param str ap_ssid: SSID/Name for Access point mode
        :param str ap_pass: Password for incoming connections in Access point mode
        :param int timeout: Time before aborting connection to access point
        """
        self.sta = STA(sta_ssid, sta_pass, timeout)
        self.ap = AP(ap_ssid, ap_pass)

        
        
        