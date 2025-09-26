from dependency_injector import containers, providers
from app.database.postgres import PostgresConnector


__all__ = ["PostgresContainer"]


class PostgresContainer(containers.DeclarativeContainer):

    config = providers.Dependency()
    connector = providers.Singleton(PostgresConnector, config)
