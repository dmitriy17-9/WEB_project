import datetime
import sqlalchemy
from flask_login import UserMixin

from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin):
    """
    Модель Пользователи
    """
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # айди
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # имя пользователя
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # описание
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)  # адрес почты
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # должность
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # пароль
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)  # дата создания

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
