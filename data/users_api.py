import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users': [item.to_dict(only=(
                'name', 'about', 'email', 'position', 'hashed_password', 'created_date'
            )) for item in users]
        }
    )


@blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=(
                'name', 'about', 'email', 'position', 'hashed_password', 'created_date'
            ))
        }
    )


@blueprint.route('/api/user', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in [
        'name', 'about', 'email', 'position', 'hashed_password'
    ]):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = User(
        name=request.json['name'],
        about=request.json['about'],
        email=request.json['email'],
        position=request.json['position'],
        hashed_password=request.json['hashed_password']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})