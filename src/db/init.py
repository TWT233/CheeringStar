import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import conf, CONF_DIR

SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(CONF_DIR, conf['db']['path'])

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

db = SessionLocal()


def get_db():
    return db
