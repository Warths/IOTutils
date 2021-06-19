from network import WLAN, AP_IF


class AP:
    def __init__(self, SSID, PASS=""):
        """
        WIFI Access point
        :param str SSID: Access point Name
        :param str PASS: Access point Password
        """
        self.SSID = SSID
        self.PASS = PASS
        self.IF = WLAN(AP_IF)

    def open(self):
        """
        Open the Access point to outside WIFI devices 
        """
        self.IF.active(True)

        config = {
            "essid": self.SSID,
            "authmode": 0,
        }

        # Handling wrong password
        if len(self.PASS) < 8:
            print("WARNING: Access Point Password must be 8 character long.")
            print("Opening Access point without password")
        else:
            config["password"] = self.PASS

        self.IF.config(**config)

    def close(self):
        """
        Closes the access point
        """
        self.IF.active(False)
