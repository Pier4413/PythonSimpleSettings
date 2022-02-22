from configparser import ConfigParser

class Settings():
    """
        This class manage the settings from a file using a Singleton

        :author: Panda <panda@delmasweb.net>
        :date: February 7, 2022
        :version: 1.0
    """

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

    def loadSettings(self, settings_file : str = "./settings.ini") -> None:
        """
            This function load the settings from a file

            :param settingsFile: Optional; Default : ./settings.ini; The settings file path (relative or absolute)
            :type settingsFile: str
        """
        self.__fileName = settings_file
        self.__configur = ConfigParser()
        self.__configur.read(settings_file)

    def get(self, section : str, option : str, default_value : str) -> None:
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: str
        """
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.get(section, option)
            else:
                return default_value
        else:
            return default_value

    def getint(self, section : str, option : str, default_value : int) -> None:
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: int
        """
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.getint(section, option)
            else:
                return default_value
        else:
            return default_value

    def getboolean(self, section : str, option : str, default_value : bool) -> None:
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: bool
        """
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.getboolean(section, option)
            else:
                return default_value
        else:
            return default_value

    def getfloat(self, section : str, option : str, default_value : float) -> None:
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: float
        """
        if(self.__configur.has_section(section) == True):
            if(self.__configur.has_option(section, option) == True):
                return self.__configur.getfloat(section, option)
            else:
                return default_value
        else:
            return default_value

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