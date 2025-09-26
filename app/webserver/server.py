import asyncio
import sys
import fastapi


__all__ = ("create_app",)


def __system_setup():
    # Windows aiopg workaround
    if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def create_app(config):
    __system_setup()
    app = fastapi.FastAPI()
    return app
