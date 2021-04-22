import flask
from flask import jsonify, request

from . import db_session
from .genres import Genre

blueprint = flask.Blueprint(
    'genres_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/genres')
def get_genres():
    db_sess = db_session.create_session()
    genres = db_sess.query(Genre).all()
    return jsonify(
        {
            'genres': [item.to_dict(only=('name', 'is_for_kids')) for item in genres]
        }
    )


@blueprint.route('/api/genre/<int:genre_id>', methods=['GET'])
def get_one_genre(genre_id):
    db_sess = db_session.create_session()
    genre = db_sess.query(Genre).get(genre_id)
    if not genre:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'genre': genre.to_dict(only=('name', 'is_for_kids'))
        }
    )


@blueprint.route('/api/genre', methods=['POST'])
def create_genre():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['name', 'is_for_kids']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    genre = Genre(
        name=request.json['name'],
        is_for_kids=request.json['is_for_kids']
    )
    db_sess.add(genre)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/genre/<int:genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    db_sess = db_session.create_session()
    genre = db_sess.query(Genre).get(genre_id)
    if not genre:
        return jsonify({'error': 'Not found'})
    db_sess.delete(genre)
    db_sess.commit()
    return jsonify({'success': 'OK'})