import uvicorn
import argparse

from app.loader import load_config
from app.webserver import create_app
from app.constants import DEFAULT_CONFIG_PATH


def start(
    env_path: str|None = None
):
    if not env_path:
        env_path = DEFAULT_CONFIG_PATH
    config = load_config(env_path)
    if not config:
        # TODO: error logging
        print("No config file found")
        return
    app = create_app(config)

    uvicorn.run(app, host=config["APP_HOST"], port=config["APP_PORT"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--env', help="Path to .env file", default=None)
    # parser.add_argument('--perform-migrations', action='store_true', default=False)
    args = parser.parse_args()

    start(args.env)
