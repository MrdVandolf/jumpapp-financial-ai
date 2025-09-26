from fastapi.templating import Jinja2Templates
from dependency_injector import containers, providers

from app.database.container import PostgresContainer


__all__ = ("AppContainer",)


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[__name__])
    app_container = providers.Self()

    config = providers.Dependency()

    postgres_container = providers.Container(
        PostgresContainer,
        config=config,
    )
