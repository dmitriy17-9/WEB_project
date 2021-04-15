import random

from flask import Flask, render_template, redirect
from data import db_session
from data.add_data_db import add_genres, add_admin, add_books
from data.books import Book
from data.genres import Genre
from data.users import User
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    """Главная страница библиотеки Library.net"""
    db_sess = db_session.create_session()
    books = db_sess.query(Book).all()
    books2 = db_sess.query(Book).all()
    if len(books) > 4:
        return render_template("index.html", books=random.choices(books, k=4), title='Library.net')
    else:
        return render_template("index.html", books=random.choices(books, k=len(books)), title='Library.net')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    """Регистрация"""
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data,
            position='user'
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Авторизация"""
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    """Выход из профиля"""
    logout_user()
    return redirect("/")


@app.route("/books")
def books():
    """Список книг"""
    db_sess = db_session.create_session()
    books = db_sess.query(Book).all()
    return render_template("books.html", books=books, title='Список книг')


@app.route("/users")
def users():
    """Список пользователей """
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return render_template("users.html", users=users, title='Список пользователей')


@app.route("/genres")
def genres():
    """Список жанров"""
    db_sess = db_session.create_session()
    genres = db_sess.query(Genre).all()
    return render_template("genres.html", genres=genres, title='Список жанров')


@app.route('/my_profile')
def my_profile():
    """Страница своего профиля"""
    return render_template("my_profile.html", tutle='Мой профиль')


def main():
    db_session.global_init("db/library.db")

    # add_genres()
    # add_admin()
    # add_books()

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()