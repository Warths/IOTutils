from . import PersistentData

class PersistentFloat(PersistentData):
    
    """
    Float persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into an integer
        """
        value = str(value)
        value = value.replace(",", ".")
        return float(value)

