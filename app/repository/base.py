from abc import ABC

__all__ = ("BaseRepository",)


class BaseRepository(ABC):

    def __init__(self, database_container):
        self.connector = database_container.connector()

    async def create(self, *args, **kwargs):
        raise NotImplementedError()

    async def read(self, *args, **kwargs):
        raise NotImplementedError()

    async def list(self, *args, **kwargs):
        raise NotImplementedError()

    async def update(self, *args, **kwargs):
        raise NotImplementedError()

    async def delete(self, *args, **kwargs):
        raise NotImplementedError()
