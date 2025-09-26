from dependency_injector import containers, providers
from app.migrations.postgres import postgres_migrate


__all__ = ["MigrationsContainer"]


class MigrationsContainer(containers.DeclarativeContainer):
    postgres_container = providers.Dependency()
    postgres_migrate = providers.Coroutine(
        postgres_migrate,
        postgres_container=postgres_container,
    )
