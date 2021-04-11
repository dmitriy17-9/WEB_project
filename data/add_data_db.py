from data import db_session
from data.genres import Genre
from data.users import User


def add_genres():
    db_sess = db_session.create_session()

    genre = Genre()
    genre.name = 'Фантастика'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Фэнтези'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Детективы'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Приключения'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Любовные романы'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Наука и образование'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Справочники и энциклопедии'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Ужасы'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Мистика'
    db_sess.add(genre)

    genre = Genre()
    genre.name = 'Проза'
    db_sess.add(genre)

    db_sess.commit()


def add_admin():
    db_sess = db_session.create_session()

    admin = User()
    admin.name = 'Admin'
    admin.about = 'Админ сайта Library.net'
    admin.email = 'admin-library@library.ru'
    db_sess.add(admin)

    db_sess.commit()
