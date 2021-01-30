from database.db_session import global_init
from flask import Flask
from controllers import user_api

if __name__ == "__main__":
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.register_blueprint(user_api.blueprint)
    global_init("sqlite:///database/users.db")
    app.run()