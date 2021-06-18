from . import PersistentData

class PersistentFloat(PersistentData):
    
    """
    Float persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into a float
        :param str value: Value to sanitize 
        :return: float converted from a string
        :rtype: float
        
        :example:
        
        >>> value="1,96"
        >>> sanityze(value)
        1.96
        """
        value = str(value)
        value = value.replace(",", ".")
        return float(value)

