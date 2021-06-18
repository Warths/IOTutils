from . import PersistentData

class PersistentString(PersistentData):
    
    """
    String persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into a string
        :param str value: Value to sanitize 
        :return: string converted from any value
        :rtype: str
        
        :example:
        
        >>> value=1234
        >>> sanityze(value)
        "1234"
        """
        return str(value)

