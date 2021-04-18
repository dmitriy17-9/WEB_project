import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Genre(SqlAlchemyBase):
    """Модель Жанры"""
    __tablename__ = 'genres'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # айди жанра
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)  # название жанра

    books = orm.relation("Book", back_populates='genre')
