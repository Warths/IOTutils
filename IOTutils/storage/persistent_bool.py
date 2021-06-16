from . import PersistentData

class PersistentBool(PersistentData):
    
    """
    Boolean persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into a boolean
        """
        return str(value).lower() not in ["none", "false", "0", "null", "no"]
