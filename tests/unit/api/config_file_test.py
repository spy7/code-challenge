from unittest import TestCase
from unittest.mock import MagicMock, patch

from code_challenge.api.config_file import ConfigFile
from code_challenge.api.settings import Settings


@patch("code_challenge.api.config_file.os", MagicMock())
@patch("code_challenge.api.config_file.open", MagicMock())
@patch("code_challenge.api.config_file.Path", MagicMock())
class ConfigFileTestCase(TestCase):
    @patch("code_challenge.api.config_file.configparser.ConfigParser")
    def test_read(self, configparser) -> None:
        file = {"api": {"Host": "local", "Endpoint": "graph", "Token": "123"}}
        configparser.return_value.__getitem__.side_effect = file.__getitem__
        configparser.return_value.__contains__.return_value = True

        settings = ConfigFile().read()

        self.assertEqual("local", settings.host)
        self.assertEqual("graph", settings.endpoint)
        self.assertEqual("123", settings.token)

    @patch("code_challenge.api.config_file.configparser.ConfigParser")
    def test_write(self, configparser):
        file = {}
        configparser.return_value.__setitem__.side_effect = file.__setitem__

        settings = Settings()
        settings.host = "localhost"
        settings.endpoint = "api"
        settings.token = "555"

        ConfigFile().write(settings)

        self.assertEqual("localhost", file["api"]["Host"])
        self.assertEqual("api", file["api"]["Endpoint"])
        self.assertEqual("555", file["api"]["Token"])
