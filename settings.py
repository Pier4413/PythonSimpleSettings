from configparser import ConfigParser
from xmlrpc.client import boolean

class Settings(ConfigParser):
    
    """
        Static instance for Singleton

        :meta static:
        :type __instance: Logger
    """
    __instance = None

    def getInstance():
        """ 
            Static access method

            :meta static:
        """
        if Settings.__instance == None:
            Settings()
        return Settings.__instance
   
    def __init__(self):
        """
            Virtually private constructor
        """
        if Settings.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Settings.__instance = self

    def loadSettings(self, settingsFile : str = "./settings.ini") -> None:
        self.__fileName = settingsFile
        self.read(settingsFile)

    def get(self, section : str, option : str, defaultValue : str) -> None:
        """
            This function returns the value of the option in the section if exists or defaultValue otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param defaultValue: The default value
            :type defaultValue: str
        """
        if(self.has_option(section, option) == True):
            return super().get(section, option)
        else:
            return defaultValue

    def getint(self, section : str, option : str, defaultValue : int) -> None:
        """
            This function returns the value of the option in the section if exists or defaultValue otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param defaultValue: The default value
            :type defaultValue: int
        """
        if(self.has_option(section, option) == True):
            return super().getint(section, option)
        else:
            return defaultValue

    def getboolean(self, section : str, option : str, defaultValue : bool) -> None:
        """
            This function returns the value of the option in the section if exists or defaultValue otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param defaultValue: The default value
            :type defaultValue: bool
        """
        if(self.has_option(section, option) == True):
            return super().getboolean(section, option)
        else:
            return defaultValue

    def getfloat(self, section : str, option : str, defaultValue : float) -> None:
        """
            This function returns the value of the option in the section if exists or defaultValue otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param defaultValue: The default value
            :type defaultValue: float
        """
        if(self.has_option(section, option) == True):
            return super().getfloat(section, option)
        else:
            return defaultValue