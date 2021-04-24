from flask import jsonify

from data import db_session
from data.books import Book
from flask_restful import abort, Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('author', required=True)
parser.add_argument('author', required=True, type=int)
parser.add_argument('file', required=True)
parser.add_argument('cover', required=True)


class BooksResource(Resource):
    def get(self, books_id):
        abort_if_books_not_found(books_id)
        session = db_session.create_session()
        books = session.query(Book).get(books_id)
        return jsonify({'books': books.to_dict(
            only=('name', 'author', 'author', 'file', 'cover'))})

    def delete(self, books_id):
        abort_if_books_not_found(books_id)
        session = db_session.create_session()
        books = session.query(Book).get(books_id)
        session.delete(books)
        session.commit()
        return jsonify({'success': 'OK'})


class BooksListResource(Resource):
    def get(self):
        session = db_session.create_session()
        books = session.query(Book).all()
        return jsonify({'genres': [item.to_dict(
            only=('name', 'author', 'author', 'file', 'cover')) for item in books]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        books = Book(
            name=args['name'],
            author=args['author'],
            genre_id=args['genre_id'],
            file=args['file'],
            cover=args['cover']
        )
        session.add(books)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_books_not_found(books_id):
    session = db_session.create_session()
    books = session.query(Book).get(books_id)
    if not books:
        abort(404, message=f"Books {books_id} not found")