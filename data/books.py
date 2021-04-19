import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Book(SqlAlchemyBase):
    """Модель Книги"""
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # айди
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # название
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # автор
    genre_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("genres.id"))  # жанр
    file = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # файл
    cover = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # обложки

    genre = orm.relation("Genre")