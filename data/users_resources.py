from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

from . import db_session
from .users import User

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('about', required=True)
parser.add_argument('email', required=True)
parser.add_argument('position', required=True)
parser.add_argument('hashed_password', required=True)
parser.add_argument('created_date', required=False)


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users':
                            [item.to_dict(only=(
                                'name', 'about', 'email', 'position', 'hashed_password', 'created_date'
                            )) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(User).filter(User.email == args['email']).first()
        if user:
            abort(418, message=f"User {args['email']} is already exist")
        user = User(
            name=args['name'],
            about=args['about'],
            email=args['email'],
            position=args['position'],
            hashed_password=args['hashed_password'],
            created_date=args['created_date']
        )
        user.set_password(user.hashed_password)
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'users': user.to_dict((
                                'name', 'about', 'email', 'position', 'hashed_password', 'created_date'
                            ))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")
