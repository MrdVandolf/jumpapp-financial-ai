import fastapi


__all__ = ("create_app",)


def create_app(config, app_container):
    app = fastapi.FastAPI()
    app.container = app_container
    return app
