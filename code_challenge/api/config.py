from code_challenge.api.config_file import ConfigFile


"""Configurate API settings"""


def config(key: str, value: str):
    ConfigFile().read()
