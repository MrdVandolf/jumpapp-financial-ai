from dependency_injector import containers, providers
from app.service.user import UserService


__all__ = ("ServiceContainer",)


class ServiceContainer(containers.DeclarativeContainer):

    config = providers.Dependency()
    repository_container = providers.Dependency()
    user_service = providers.Factory(
        UserService,
        config=config,
        repository_container=repository_container,
    )
