from code_challenge.api.config_file import ConfigFile

"""Configurate API settings"""


def config(key: str, value: str) -> None:
    settings = ConfigFile().read()
    if not hasattr(settings, key):
        raise KeyError(f"Invalid key: {key}")
    setattr(settings, key, value)
    ConfigFile().write(settings)
