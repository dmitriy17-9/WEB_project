import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Genre(SqlAlchemyBase, SerializerMixin):
    """Модель Жанры"""
    __tablename__ = 'genres'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # айди жанра
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)  # название жанра
    is_for_kids = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)

    books = orm.relation("Book", back_populates='genre')
