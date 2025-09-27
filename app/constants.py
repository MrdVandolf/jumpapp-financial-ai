import logging


__all__ = ("DEFAULT_CONFIG_PATH", "DEFAULT_LOGGER_FILE", "DEFAULT_LOGGER_LEVEL",
           "LOGGER_LEVELS", "DEFAULT_JWT_COOKIE", "DEFAULT_JWT_LIFETIME",)

DEFAULT_CONFIG_PATH = "config/.env"

DEFAULT_LOGGER_FILE = "logs/main.log"
DEFAULT_LOGGER_LEVEL = logging.WARNING
LOGGER_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
}

DEFAULT_JWT_COOKIE = "4cc355"
DEFAULT_JWT_LIFETIME = 3600  # in seconds
