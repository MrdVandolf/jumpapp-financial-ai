import fastapi
from contextlib import asynccontextmanager
from starlette.staticfiles import StaticFiles


__all__ = ("create_app",)


async def __perform_migrations(app):
    app_container = app.container
    await app_container.migrations_container.postgres_migrate(execute_migrations=app.execute_migrations)


@asynccontextmanager
async def lifespan(app):
    await __perform_migrations(app)
    yield


def create_app(
    config,
    app_container,
    execute_migrations: bool,
    routers: list[fastapi.APIRouter],
) -> fastapi.FastAPI:
    app = fastapi.FastAPI(lifespan=lifespan)

    # app variables - container and misc data
    app.container = app_container
    app.execute_migrations = execute_migrations

    # route wiring
    for router in routers:
        app.include_router(router)

    # static wiring
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app
