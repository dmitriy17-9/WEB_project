from data import db_session
from data.books import Book
from data.genres import Genre
from data.users import User


def add_admin():
    """Добавление админа"""
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
    """Добавление жанров"""
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
    """Добавление книг"""
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


def add_users():
    db_sess = db_session.create_session()

    user1 = User()
    user1.name = 'Some user'
    user1.about = 'User for Library.net'
    user1.email = 'user1cool@ya.ru'
    user1.position = 'user'
    user1.set_password('user123')

    user2 = User()
    user2.name = 'Cool user'
    user2.about = 'Nothing'
    user2.email = 'user2qwerty@ya.ru'
    user2.position = 'user'
    user2.set_password('user234')

    user3 = User()
    user3.name = 'User'
    user3.about = ')))'
    user3.email = 'skobochka@ya.ru'
    user3.position = 'user'
    user3.set_password('user345')

    user4 = User()
    user4.name = 'Resu'
    user4.about = ':)'
    user4.email = 'smile@ya.ru'
    user4.position = 'user'
    user4.set_password('user456')

    user5 = User()
    user5.name = 'cube'
    user5.about = 'it-cube'
    user5.email = 'itcubeya@ya.ru'
    user5.position = 'user'
    user5.set_password('user567')

    user6 = User()
    user6.name = 'User6'
    user6.about = 'Haha'
    user6.email = 'funnyuser@ya.ru'
    user6.position = 'user'
    user6.set_password('user678')

    user7 = User()
    user7.name = 'person'
    user7.about = 'some person'
    user7.email = 'personlibrary@ya.ru'
    user7.position = 'user'
    user7.set_password('user789')

    db_sess.add_all([user1, user2, user3, user4, user5, user6, user7])

    db_sess.commit()