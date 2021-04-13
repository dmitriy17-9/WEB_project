import os

from data import db_session
from data.books import Book
from data.convert_to_binary import convert_to_binary
from data.genres import Genre
from data.users import User


def add_admin():
    db_sess = db_session.create_session()

    admin = User()
    admin.name = 'Admin'
    admin.about = 'Админ сайта Library.net'
    admin.email = 'admin-library@library.ru'
    admin.set_password('adminl1')
    db_sess.add(admin)

    db_sess.commit()


def add_genres():
    db_sess = db_session.create_session()
    db_sess.add_all([
        Genre(name='Фантастика'),
        Genre(name='Фэнтези'),
        Genre(name='Детективы'),
        Genre(name='Приключения'),
        Genre(name='Любовные романы'),
        Genre(name='Наука и образование'),
        Genre(name='Справочники и энциклопедии'),
        Genre(name='Ужасы и мистика'),
        Genre(name='Проза')
    ])
    db_sess.commit()


def add_books():
    db_sess = db_session.create_session()

    book = Book()
    book.name = 'Бегущий в лабиринте'
    book.author = 'Джеймс Дэшнер'
    book.genre_id = 1
    os.chdir('static/pdf')
    book.file = convert_to_binary('The_Maze_Runner.pdf')
    os.chdir('../img')
    book.cover = convert_to_binary('The_Maze_Runner.png')
    db_sess.add(book)

    book = Book()
    book.name = 'Испытание огнем'
    book.author = 'Джеймс Дэшнер'
    book.genre_id = 1
    os.chdir('../pdf')
    book.file = convert_to_binary('The_Scorch_Trials.pdf')
    os.chdir('../img')
    book.cover = convert_to_binary('The_Maze_Runner.png')
    db_sess.add(book)

    db_sess.commit()


