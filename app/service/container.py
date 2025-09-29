from dependency_injector import containers, providers
from app.service.user import UserService
from app.service.ai import AiService
from app.service.google import GoogleService


__all__ = ("ServiceContainer",)


class ServiceContainer(containers.DeclarativeContainer):

    config = providers.Dependency()
    repository_container = providers.Dependency()
    user_service = providers.Factory(
        UserService,
        config=config,
        repository_container=repository_container,
    )
    ai_service = providers.Factory(
        AiService,
        config=config,
    )
    google_service = providers.Factory(
        GoogleService,
        config=config,
    )
