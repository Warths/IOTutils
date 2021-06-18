from . import PersistentFloat

class PersistentInteger(PersistentFloat):
    
    """
    Integer persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into an integer
        :param str value: Value to sanitize 
        :return: int converted from a string
        :rtype: int
        
        :example:
        
        >>> value="1.0"
        >>> sanityze(value)
        1
        """
        return int(super().sanityze(value))
