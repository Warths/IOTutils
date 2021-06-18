import os

class PersistentData:
    def __init__(self, name, default="", folder="STORAGE"):
        """
        PersistentData can be used as persistent config files
        This is the base class that can be used to expand the functionnality
        to include data types.
        
        :param str name: name of the file storing the data
        :param str default: default value if the file doesn't exists
        :param str folder: folder where the file is used
        """
        self.name = name
        self.folder = folder
        self.default = default
        
    def mkdir(self):
        """
        Create the folder of the persistent data
        """
        try:
            os.mkdir(self.folder)
        except OSError:
            pass
    
    @property
    def path(self):
        """
        Path to file
        :return: path to file
        :rtype: str
        """
        return "/" + self.folder + "/" + self.name
        
    def read(self):
        """
        Return the content of the file or default value in case of failure
        :return: content of the file or self.default
        :rtype: str
        """
        try:
            with open(self.path, "r") as file:
                return file.read()
        except OSError:
                return self.default
            
    def write(self, value):
        """
        Write the value in the file.
        Str cast to prevent buffer error
        """
        self.mkdir()
        with open(self.path, "w") as file:
             file.write(str(value))
    
    @property
    def value(self):
        """
        File value getter
        :return: sanityzed value.
        :rtype: depends on sanityze()
        """
        return self.sanityze(self.read())
        
    @value.setter
    def value(self, value):
        """
        File value setter
        :param value: Value to write into the file
        """
        self.write(self.sanityze(value))
    
    def sanityze(self, value):
         """
         Sanitize value to fit data type.
         This method is there to be overloaded by child class
         :param value: Value to sanityze
         """
         return value
