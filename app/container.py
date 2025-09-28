from fastapi.templating import Jinja2Templates
from dependency_injector import containers, providers

from app.database.container import PostgresContainer
from app.migrations.container import MigrationsContainer
from app.repository.container import RepositoryContainer
from app.service.container import ServiceContainer


__all__ = ("AppContainer",)


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[__name__])
    app_container = providers.Self()

    config = providers.Dependency()

    templates = providers.Singleton(
        Jinja2Templates,
        directory="app/templates",
    )

    postgres_container = providers.Container(
        PostgresContainer,
        config=config,
    )

    migrations_container = providers.Container(
        MigrationsContainer,
        postgres_container=postgres_container,
    )

    repository_container = providers.Container(
        RepositoryContainer,
        postgres_container=postgres_container,
    )

    service_container = providers.Container(
        ServiceContainer,
        config=config,
        repository_container=repository_container,
    )
