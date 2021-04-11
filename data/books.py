import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Book(SqlAlchemyBase):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    genre_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("genres.name"), nullable=True)
    file = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=True)
    cover = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=True)

    genre = orm.relation("Genre")