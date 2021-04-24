import os
import random

from flask import Flask, render_template, redirect, request, abort, make_response, jsonify
from waitress import serve

from data import db_session, books_api, genres_api, users_api, genres_resources, users_resources, books_resources
from data.add_data_db import add_genres, add_admin, add_books, add_users
from data.books import Book
from data.genres import Genre
from data.users import User
from forms.genres import GenresForm
from forms.user import RegisterForm, LoginForm, EditForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import abort, Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api = Api(app)
api.add_resource(genres_resources.GenresListResource, '/api/v2/genres')
api.add_resource(genres_resources.GenresResource, '/api/v2/genres/<int:genres_id>')

api.add_resource(books_resources.BooksListResource, '/api/v2/books')
api.add_resource(books_resources.BooksResource, '/api/v2/books/<int:books_id>')

api.add_resource(users_resources.UsersListResource, '/api/v2/users')
api.add_resource(users_resources.UserResource, '/api/v2/users/<int:users_id>')

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
    if len(books) > 4:
        return render_template("index.html",
                               books=random.choices(books, k=4),
                               title='Library.net')
    else:
        return render_template("index.html",
                               books=random.choices(books, k=len(books)),
                               title='Library.net')


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


@app.route("/genres", methods=['GET', 'POST'])
def genres():
    """Список жанров"""
    db_sess = db_session.create_session()
    genres = db_sess.query(Genre).all()
    form = GenresForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        genre = Genre()
        genre.name = form.name.data
        db_sess.add(genre)
        db_sess.commit()
        return redirect('/')
    return render_template("genres.html", genres=genres, title='Список жанров', form=form)


@app.route('/my_profile', methods=['GET', 'POST'])
@login_required
def my_profile():
    """Страница своего профиля"""
    form = EditForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        me = db_sess.query(User).filter(User.id == current_user.id).first()
        if me:
            form.name.data = me.name
            form.about.data = me.about
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        if user:
            user.name = form.name.data
            user.about = form.about.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template("my_profile.html",
                           tutle='Мой профиль',
                           form=form)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/library.db")

    # add_admin()
    # add_users()
    # add_genres()
    # add_books()

    app.register_blueprint(books_api.blueprint)
    app.register_blueprint(genres_api.blueprint)
    app.register_blueprint(users_api.blueprint)

    port = int(os.environ.get('PORT', 5000))
    serve(app, port=port, host="0.0.0.0")


if __name__ == '__main__':
    main()
