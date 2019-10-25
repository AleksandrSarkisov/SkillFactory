from bottle import route
from bottle import run
from bottle import HTTPError

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///albums.sqlite3"

#Базыовый класс моделей таблиц
Base = declarative_base()

class Albums(Base):
    """
    Описывает структуру таблицы albums для хранения записей музыкальной библиотеки
    """
    # Указываем имя таблицы
    __tableName__ = "album"
    # Идентификатор строки
    id = sa.Column(sa.INTEGER, primary_key=True)
    # Год выпуска альбома
    year = sa.Column(sa.INTEGER)
    # Артист или группа
    artist = sa.Column(sa.TEXT)
    # Жанр альбома
    genre = sa.Column(sa.TEXT)
    # Название альбома
    album = sa.Column(sa.TEXT)

def connect_db():
    """
    Подключаемся к БД albums.sqllite3
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем фабрику сессию
    Session = sessionmaker(engine)
    # создаем сессию
    session = Session()
    return session

def find(artist, session):
    # находим все записи в таблице album, у которых поле album.artist совпадает с параметром artist
    query = session.query(Album).filter(Album.artist == artist)
    # вычисляем количество таких записей
    albumsCount = query.count()
    return (albumsCount, [query.album for query in query.all()])


@route("/albums/<artist>")
def albums(artist):
    '''
    Принимает название группы или артиста и выдает в первой строке количество альбомов и список в каждой отдельной строке название альбомов.
    '''
    count, albums = find(artist, connect_db())
    if count == 0:
        message = "Албомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        result = "Количество альбомов {} - {}\n".format(artist, count)
        result += "\n".join(albums)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
