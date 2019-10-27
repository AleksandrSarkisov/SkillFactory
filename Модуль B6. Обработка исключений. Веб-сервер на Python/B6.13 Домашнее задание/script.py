from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

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
    __tablename__ = "album"
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

    def __eq__(self, other):
        if self.year == other.year and self.artist == other.artist and self.genre == other.genre and self.album == other.album:
            return True
        else:
            return False

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

def find_artist(artist, session):
    # находим все записи в таблице album, у которых поле album.artist совпадает с параметром artist
    query = session.query(Albums).filter(Albums.artist == artist)
    # вычисляем количество таких записей
    albumsCount = query.count()
    return (albumsCount, [query.album for query in query.all()])

def save_album(album_data, session):
    """
    Записывает новую запись в БД
    """
    ex = Albums(year = album_data["year"], artist = album_data["artist"], genre = album_data["genre"], album = album_data["album"])
    q = session.query(Albums).filter(Albums.year == ex.year, Albums.artist == ex.artist, Albums.genre == ex.genre, Albums.album == ex.album)
    if q.count() == 0:
        session.add(ex)
        session.commit()
        return True
    return False

def check_data(album_data):
    """
    Проверяет тип параметра year, которрое должно быть целочисленным и все передаваемые данные должны быть не None
    """
    for key in album_data.keys():
        if album_data[key] is None:
            return (False, "Неверное значение параметра {}".format(key))
    try:
        int(album_data["year"])
    except ValueError:
        return (False, "Неверное значение параметра year")
    return (True, "")

@route("/albums/<artist>")
def albums(artist):
    '''
    Принимает название группы или артиста и выдает в первой строке количество альбомов и список в каждой отдельной строке название альбомов.
    '''
    count, albums = find_artist(artist, connect_db())
    if count == 0:
        message = "Албомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        result = "Количество альбомов {} - {}<br>".format(artist, count)
        result += "<br>".join(albums)
    return result

@route("/albums", method="POST")
def add_album():
    album_data = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album"),
    }
    flag, message = check_data(album_data)
    if flag:
        album_data["year"] = int(album_data["year"])
        flag = save_album(album_data, connect_db())
        if flag:
            result = "Альбом {} записан".format(album_data["album"])
        else:
            message = "Повторная запись"
            result = HTTPError(409, message)
    else:
        result = HTTPError(415, message)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
