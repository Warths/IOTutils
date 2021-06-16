from . import PersistentFloat

class PersistentInteger(PersistentFloat):
    
    """
    Integer persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into an integer
        """
        return int(super().sanityze(value))
