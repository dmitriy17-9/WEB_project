import flask
from flask import jsonify, request

from . import db_session
from .books import Book

blueprint = flask.Blueprint(
    'books_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/books')
def get_books():
    db_sess = db_session.create_session()
    books = db_sess.query(Book).all()
    return jsonify(
        {
            'books':
                [item.to_dict(only=(
                'name', 'author', 'genre.name', 'file', 'cover'))
                 for item in books]
        }
    )


@blueprint.route('/api/book/<int:book_id>', methods=['GET'])
def get_one_book(book_id):
    db_sess = db_session.create_session()
    book = db_sess.query(Book).get(book_id)
    if not book:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'book': book.to_dict(only=(
                'name', 'author', 'genre.name', 'file', 'cover'))
        }
    )


@blueprint.route('/api/book', methods=['POST'])
def create_books():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'author', 'genre_id', 'file', 'cover']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    books = Book(
        name=request.json['name'],
        author=request.json['author'],
        genre_id=request.json['genre_id'],
        file=request.json['file'],
        cover=request.json['cover']
    )
    db_sess.add(books)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    db_sess = db_session.create_session()
    book = db_sess.query(Book).get(book_id)
    print(book_id, book)
    if not book:
        return jsonify({'error': 'Not found'})
    db_sess.delete(book)
    db_sess.commit()
    return jsonify({'success': 'OK'})