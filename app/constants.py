import logging


__all__ = ("DEFAULT_CONFIG_PATH",)

DEFAULT_CONFIG_PATH = "config/.env"

DEFAULT_LOGGER_FILE = "logs/main.log"
DEFAULT_LOGGER_LEVEL = logging.WARNING
LOGGER_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
}
