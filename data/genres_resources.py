from flask import jsonify

from data import db_session
from data.genres import Genre
from flask_restful import abort, Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('is_for_kids', required=True, type=bool)


class GenresResource(Resource):
    def get(self, genres_id):
        abort_if_genres_not_found(genres_id)
        session = db_session.create_session()
        genres = session.query(Genre).get(genres_id)
        return jsonify({'genres': genres.to_dict(
            only=('name', 'is_for_kids'))})

    def delete(self, genres_id):
        abort_if_genres_not_found(genres_id)
        session = db_session.create_session()
        genres = session.query(Genre).get(genres_id)
        session.delete(genres)
        session.commit()
        return jsonify({'success': 'OK'})


class GenresListResource(Resource):
    def get(self):
        session = db_session.create_session()
        genres = session.query(Genre).all()
        return jsonify({'genres': [item.to_dict(
            only=('name', 'is_for_kids')) for item in genres]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        genres = Genre(
            name=args['name'],
            is_for_kids=args['is_for_kids']
        )
        session.add(genres)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_genres_not_found(genres_id):
    session = db_session.create_session()
    genres = session.query(Genre).get(genres_id)
    if not genres:
        abort(404, message=f"Genres {genres_id} not found")