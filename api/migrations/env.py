import os
import sys
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context


parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_dir)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
fileConfig(config.config_file_name)
sys.path.insert(0, os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))
))

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

from api.database import Base
from api.models import *

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', 'api')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'postgres')
DATABASE_URL = os.environ.get('DATABASE_URL', 'db')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 5432)
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'data')

SQLALCHEMY_DATABASE_URL = (f"postgresql://{DATABASE_USERNAME}:"
                           f"{DATABASE_PASSWORD}@{DATABASE_URL}:"
                           f"{DATABASE_PORT}/{DATABASE_NAME}")


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    print(SQLALCHEMY_DATABASE_URL)
    context.configure(
        url=SQLALCHEMY_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    print(SQLALCHEMY_DATABASE_URL)
    connectable = create_engine(
        SQLALCHEMY_DATABASE_URL,
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
