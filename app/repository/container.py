from dependency_injector import containers, providers
from app.repository.users import UsersRepository
from app.repository.chats import ChatsRepository


__all__ = ("RepositoryContainer",)

class RepositoryContainer(containers.DeclarativeContainer):

    postgres_container = providers.Dependency()
    users = providers.Factory(UsersRepository, postgres_container)
    chats = providers.Factory(ChatsRepository, postgres_container)
