import configparser
import os
from pathlib import Path

from code_challenge.api.settings import Settings


class ConfigFile:
    """ConfigFile class to read and update settings from a file"""

    folder: str = ".config/code_challenge"
    filename: str = "config.ini"

    def get_path(self) -> str:
        return os.path.join(os.path.expanduser("~"), self.folder)

    def get_file_path(self) -> str:
        return os.path.join(self.get_path(), self.filename)

    def create_path(self) -> None:
        Path(self.get_path()).mkdir(parents=True, exist_ok=True)

    def read(self) -> Settings:
        config = configparser.ConfigParser()
        config.read(self.get_file_path())
        settings = Settings()
        if "api" in config:
            settings.host = config["api"]["Host"]
            settings.endpoint = config["api"]["Endpoint"]
            settings.token = config["api"]["Token"]
        return settings

    def write(self, settings: Settings) -> None:
        config = configparser.ConfigParser()
        config["api"] = {
            "Host": settings.host,
            "Endpoint": settings.endpoint,
            "Token": settings.token,
        }
        self.create_path()
        with open(self.get_file_path(), "w") as file:
            config.write(file)
