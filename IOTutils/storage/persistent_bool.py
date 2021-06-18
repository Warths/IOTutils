from . import PersistentData

class PersistentBool(PersistentData):
    
    """
    Boolean persistent data
    """
    
    def sanityze(self, value):
        """
        Sanityze value into a boolean
        :param str value: Value to sanitize 
        :return: Boolean converted from a string
        :rtype: bool
        
        :example:
        
        >>> value="true"
        >>> sanityze(value)
        True
        """
        return str(value).lower() not in ["none", "false", "0", "null", "no", "n"]
