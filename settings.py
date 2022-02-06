from configparser import ConfigParser
from re import S
from xmlrpc.client import boolean

class Settings():
    
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
        self.__configur = ConfigParser()
        self.__configur.read(settingsFile)

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
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.get(section, option)
            else:
                return defaultValue
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
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.getint(section, option)
            else:
                return defaultValue
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
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.getboolean(section, option)
            else:
                return defaultValue
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
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.getfloat(section, option)
            else:
                return defaultValue
        else:
            return defaultValue

    def set(self, section : str, option : str, value : str) -> None:
        """
            This function set the value of the option in the file

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param value: The value
            :type value: str
        """
        self.__configur.set(section, option, value)

    def write(self) -> None:
        """
            This function writes the settings in the file
        """
        with open(self.__fileName, encoding="utf8", mode="w") as file:
            self.__configur.write(file)