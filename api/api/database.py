from os import environ
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_USERNAME = environ.get('DATABASE_USERNAME', 'api')
DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD', 'postgres')
DATABASE_URL = environ.get('DATABASE_URL', 'db')
DATABASE_PORT = environ.get('DATABASE_PORT', 5432)
DATABASE_NAME = environ.get('DATABASE_NAME', 'data')

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}\
                            :{DATABASE_PASSWORD}@{DATABASE_URL}\
                            :{DATABASE_PORT}/{DATABASE_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
