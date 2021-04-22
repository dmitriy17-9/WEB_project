import os
from pickle import dumps

from data import db_session
from data.books import Book
from data.genres import Genre
from data.users import User


def add_admin():
    """
    Добавление админа
    :return:
    """
    db_sess = db_session.create_session()

    admin = User()
    admin.name = 'Admin'
    admin.about = 'Админ сайта Library.net'
    admin.email = 'admin-library@library.ru'
    admin.set_password('adminl1')
    admin.position = 'admin'
    db_sess.add(admin)

    db_sess.commit()


def add_genres():
    """
    Добавление жанров
    :return:
    """
    db_sess = db_session.create_session()
    db_sess.add_all([
        Genre(name='Фантастика', is_for_kids=False),
        Genre(name='Фэнтези', is_for_kids=False),
        Genre(name='Детективы', is_for_kids=False),
        Genre(name='Приключения', is_for_kids=False),
        Genre(name='Любовные романы', is_for_kids=False),
        Genre(name='Наука и образование', is_for_kids=True),
        Genre(name='Справочники и энциклопедии', is_for_kids=True),
        Genre(name='Ужасы и мистика', is_for_kids=False),
        Genre(name='Проза', is_for_kids=True),
        Genre(name='Стихотворение', is_for_kids=True),
        Genre(name='Сказка', is_for_kids=True)
    ])
    db_sess.commit()


def add_books():
    """
    Добавление книг
    :return:
    """
    db_sess = db_session.create_session()

    book = Book()
    book.name = 'Бегущий в лабиринте'
    book.author = 'Джеймс Дэшнер'
    book.genre_id = 1
    book.file = 'static/pdf/The_Maze_Runner.pdf'
    book.cover = 'static/img/The_Maze_Runner.png'
    db_sess.add(book)

    book = Book()
    book.name = 'Испытание огнем'
    book.author = 'Джеймс Дэшнер'
    book.genre_id = 1
    book.file = 'static/pdf/The_Scorch_Trials.pdf'
    book.cover = 'static/img/The_Maze_Runner.png'
    db_sess.add(book)

    db_sess.commit()
