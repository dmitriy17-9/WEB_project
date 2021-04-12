from flask import Flask, render_template
from data import db_session
from data.add_data_db import add_genres, add_admin, add_books
from data.books import Book

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    books = db_sess.query(Book).all()
    return render_template("index.html", books=books, title='Library.net')


def main():
    db_session.global_init("db/library.db")

    add_genres()
    add_admin()
    add_books()

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()