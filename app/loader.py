import logging
from logging.config import dictConfig
from dotenv import dotenv_values


__all__ = ("load_config", "load_logger")


def load_logger(log_level: int, log_file: str):
    return dictConfig(
        {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s][%(levelname)s] - %(message)s',
                }
            },
            'handlers': {
                'file': {
                    'class': 'logging.FileHandler',
                    'formatter': 'default',
                    'filename': log_file,
                    'encoding': 'utf-8',
                },
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                }
            },
            'loggers': {
                'uvicorn': {'handlers': ['file', 'console'], 'level': 'INFO', 'propagate': False},
                'uvicorn.error': {'handlers': ['file', 'console'], 'level': 'INFO', 'propagate': False},
                'uvicorn.access': {'handlers': ['file', 'console'], 'level': 'INFO', 'propagate': False},
            },
            'root': {
                'handlers': ['file', 'console'],
                'level': log_level,
            }
        }
    )


def load_config(config):
    config = dict(dotenv_values(config))
    for k, v in config.items():
        if "port" in k.lower():
            config[k] = int(v)
    return config
