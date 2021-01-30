from database.db_session import create_session, global_init
import namegenerator
from random import randint
from models.user import User

global_init("sqlite:///C:/Users/Roman/PycharmProjects/web1/database/users.db")
session = create_session()

for _ in range(100):
    st = ' '.join(map(str.capitalize,
                             namegenerator.gen().split('-')))
    print(st)
    user = User(st,
                bool(randint(0, 1)))
    session.add(user)
    print(user)
    session.commit()