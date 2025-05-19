
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

    @property
    def fileName(self) -> str:
        if self.__fileName is not None:
            return self.__fileName
        else:
            raise Exception("No filename") 

    @staticmethod
    def get_instance():
        """ 
            Static access method

            :meta static:
        """
        if Settings.__instance == None:
            Settings()
        return Settings.__instance
   
    def __init__(self : "Settings"):
        """
            Virtually private constructor
        """
        if Settings.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Settings.__instance = self
            self.load_settings()

    def load_settings(self : "Settings", settings_file : str = "./settings.ini") -> None:
        """
            This function load the settings from a file

            :param settingsFile: Optional; Default : ./settings.ini; The settings file path (relative or absolute)
            :type settingsFile: str
        """
        if settings_file is not None:
            self.__fileName = settings_file
            self.__configur = ConfigParser()
            self.__configur.read(settings_file, encoding="utf8")
        else:
            self.__fileName = None
            self.__configur = ConfigParser()

    @staticmethod
    def get(section : str, option : str, default_value : str) -> str:  # type: ignore
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: str
        """
        if Settings.get_instance() is not None and Settings.get_instance().fileName is not None and Settings.get_instance().__configur.has_section(section) is True:
            if Settings.get_instance().__configur.has_option(section, option) is True:
                return Settings.get_instance().__configur.get(section, option)
        return default_value

    @staticmethod
    def getint(section : str, option : str, default_value : int) -> int:
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: int
        """
        if Settings.get_instance().fileName is not None and Settings.get_instance().__configur.has_section(section) is True:
            if Settings.get_instance().__configur.has_option(section, option) is True:
                return Settings.get_instance().__configur.getint(section, option)
        return default_value

    @staticmethod
    def getboolean(section : str, option : str, default_value : bool) -> bool:
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: bool
        """
        if Settings.get_instance().fileName is not None and Settings.get_instance().__configur.has_section(section) is True:
            if Settings.get_instance().__configur.has_option(section, option) is True:
                return Settings.get_instance().__configur.getboolean(section, option)
        return default_value

    @staticmethod
    def getfloat(section : str, option : str, default_value : float) -> float:
        """
            This function returns the value of the option in the section if exists or default_value otherwise

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param default_value: The default value
            :type default_value: float
        """
        if Settings.get_instance().fileName is not None and Settings.get_instance().__configur.has_section(section) is True:
            if Settings.get_instance().__configur.has_option(section, option) is True:
                return Settings.get_instance().__configur.getfloat(section, option)
        return default_value

    @staticmethod
    def set(section : str, option : str, value : str) -> None:
        """
            This function set the value of the option in the file

            :param section: The section in the ini file
            :type section: str
            :param option: The option in the ini file
            :type option: str
            :param value: The value
            :type value: str
        """
        Settings.get_instance().__configur.set(section, option, value)

    @staticmethod 
    def write() -> None:
        """
            This function writes the settings in the file
        """
        with open(Settings.get_instance().fileName, encoding="utf8", mode="w") as file:
            Settings.get_instance().__configur.write(file)