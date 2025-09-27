from abc import ABC, abstractmethod
from contextlib import asynccontextmanager


__all__ = ["BaseConnector"]

class BaseConnector(ABC):

    def __init__(self, config: dict, *args, **kwargs):
        self.user = None
        self.password = None
        self.host = None
        self.port = None
        self.driver = None

    @property
    def dsn(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}"

    @abstractmethod
    @asynccontextmanager
    async def connect(self):
        raise NotImplementedError

    @abstractmethod
    @asynccontextmanager
    async def get_cursor(self):
        raise NotImplementedError()

    @abstractmethod
    async def execute(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def create_database(self):
        raise NotImplementedError()

