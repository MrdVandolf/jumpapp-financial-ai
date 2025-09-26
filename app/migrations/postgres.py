import logging


__all__ = ("postgres_migrate",)


MIGRATIONS = (
    """create table if not exists users (
       id serial primary key, 
       email text not null,
       hash text not null,
       salt text not null,
       hubspot text
    );""",
    """create table if not exists chats (
       id serial primary key, 
       user_id integer references users(id)
    );""",
    """create table if not exists messages (
       id serial primary key, 
       chat_id integer references chats(id),
       sender text not null,
       content text not null
    );""",
)


async def postgres_migrate(postgres_container, execute_migrations: bool = False):
    connector = postgres_container.connector()
    await connector.create_database()

    if execute_migrations:
        logging.info("[postgres_migrate] executing migrations...")
        for i in MIGRATIONS:
                await connector.execute(i)
        logging.info("[postgres_migrate] migration completed.")
