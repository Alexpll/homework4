from flask import Blueprint, request
from database.db_session import create_session
from models.user import User
import json


blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/', methods=['GET'])
def get_users():
    session = create_session()
    users = session.query(User)
    return json.dumps([user.to_dict() for user in users])


@blueprint.route('/<id>', methods=['GET'])
def get_user(id):
    session = create_session()
    user = session.query(User).filter(User.user_id == id).one()
    return user.to_dict()


@blueprint.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    session = create_session()
    user = User(data["full_name"], data["sex"])
    try:
        session.add(user)
        session.commit()
        return {"status": "ok"}
    except Exception as e:
        print(e)
        return {"status": "error", "error": str(e)}

