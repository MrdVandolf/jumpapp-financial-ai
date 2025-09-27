import aiopg

from contextlib import asynccontextmanager
from psycopg2.errors import DuplicateDatabase
from psycopg2.extras import RealDictCursor

from app.database.base import BaseConnector


__all__ = ("PostgresConnector",)


class PostgresConnector(BaseConnector):

    def __init__(self, config):
        super().__init__(config)
        self.user = config["POSTGRES_USER"]
        self.password = config["POSTGRES_PASSWORD"]
        self.host = config["POSTGRES_HOST"]
        self.port = config["POSTGRES_PORT"]
        self.db = config["POSTGRES_DB"]
        self.driver = "postgres"

    @property
    def dsn_db(self) -> str:
        return f"{self.dsn}/{self.db}"

    @asynccontextmanager
    async def connect(self, dsn):
        async with aiopg.connect(dsn=dsn) as connection:
            yield connection

    @asynccontextmanager
    async def get_cursor(self, dsn):
        async with self.connect(dsn) as connection:
            async with (await connection.cursor(cursor_factory=RealDictCursor)) as cursor:
                yield cursor

    async def execute(self, query, values=None, result=None):
        async with self.get_cursor(self.dsn_db) as cursor:
            await cursor.execute(query, values)
            if result == "fetchall":
                return await cursor.fetchall()
            elif result == "fetchone":
                return await cursor.fetchone()

    async def create_database(self):
        async with self.get_cursor(self.dsn) as cursor:
            try:
                await cursor.execute(f"CREATE DATABASE {self.db}")
            except DuplicateDatabase:
                # OK. means database is already in place
                return
