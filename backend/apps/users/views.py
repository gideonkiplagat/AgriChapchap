from flask import jsonify, request
from . import user_blueprint
from .models import User
from agrichap.agrichap import db

@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users]), 200

@user_blueprint.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
