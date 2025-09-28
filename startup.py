import uvicorn
import argparse
import logging
import sys
import asyncio

from app.loader import load_config, load_logger
from app.container import AppContainer
from app.webserver import create_app
from app.constants import (
    DEFAULT_CONFIG_PATH,
    DEFAULT_LOGGER_FILE,
    DEFAULT_LOGGER_LEVEL,
    LOGGER_LEVELS,
)


def start(
    env: str|None = None,
    log_level: str|None = None,
    execute_migrations: bool = False,
):
    # Windows aiopg workaround
    if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Read config
    if not env:
        env = DEFAULT_CONFIG_PATH
    config = load_config(env)
    if not config:
        logging.error("Config is empty or no config file is found")
        return

    # Configure logging
    if not log_level:
        log_level = DEFAULT_LOGGER_LEVEL
    else:
        log_level = LOGGER_LEVELS.get(log_level.lower()) or DEFAULT_LOGGER_LEVEL
    logging_config = load_logger(
        log_file=DEFAULT_LOGGER_FILE,
        log_level=log_level,
    )

    # init container
    app_container = AppContainer(config=config)
    app_container.wire()

    # create app, execute database migrations etc
    app = create_app(
        config=config,
        app_container=app_container,
        execute_migrations=execute_migrations,
    )
    uvicorn.run(app, host=config["APP_HOST"], port=config["APP_PORT"], log_config=logging_config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--env', help="Path to .env file", default=None)
    parser.add_argument('--log-level', help="Logging level", default=None)
    parser.add_argument('--execute-migrations', help="Execute database migrations or ignore them", action='store_true', default=False)
    args = parser.parse_args()

    start(
        env=args.env,
        log_level=args.log_level,
        execute_migrations=args.execute_migrations,
    )
