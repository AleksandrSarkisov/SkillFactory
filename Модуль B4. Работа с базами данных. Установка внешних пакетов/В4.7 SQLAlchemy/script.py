import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import re

os.chdir("Модуль B4. Работа с базами данных. Установка внешних пакетов\В4.7 SQLAlchemy")

DB_PATH = "sqlite:///b4_7.sqlite3"

Base = declarative_base()

class Album(Base):
    """
    Описывает структуру таблицы album дял хранения записей музыкальной библиотеки
    """
    # Наименование таблицы
    __tablename__ = "album"
    # Название колонок
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()

albums = session.query(Album).all()

def parse_connetion_string(connection_string):
    """
    Принимает на вход строку соединения connection_string и возвращает словарь с ее составными частями
    """
    pars = r'(\w+)+'
    dialect = r'(\w+)\W'
    driver = r'\+(\w*):'
    user = r'//(\w*):'
    password = r':(\w*)[@,/]'
    host = r'@(\w*)[:,/]'
    port = r':(\d*)/'
    database = r'$/(\w+\W*\w*?.\w*)'

    keys = {"dialect": dialect, "driver": driver, "user": user, "password": password, "host": host, "port": port, "database": database}
    res = {}
    for key in keys:
        res[key] = re.search(keys[key], connection_string).group(1) if re.search(keys[key], connection_string) else ""
    return res

print(parse_connetion_string("sqlite3:///b4_7.sqlite3"))
print(parse_connetion_string("postgresql+psycopg2://admin:1234@localhost/b4_7"))
print(parse_connetion_string("m2sql://admin:1234/b4_7"))
