import logging
from dotenv import dotenv_values


__all__ = ("load_config", "load_logger")


LOG_FORMATTER = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')


def load_logger(log_level: int, log_file: str):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    for handler in (console_handler, file_handler):
        handler.setFormatter(LOG_FORMATTER)
        logger.addHandler(handler)


def load_config(config):
    config = dict(dotenv_values(config))
    for k, v in config.items():
        if "port" in k.lower():
            config[k] = int(v)
    return config
