from . import PersistentData

class PersistentString(PersistentData):
    
    """
    String persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into a String
        """
        return str(value)

