from database.db_session import SqlAlchemyBase
import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, ):
    __tablename__ = "User"

    user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    full_name = sa.Column(sa.String, nullable=False, unique=True)
    sex = sa.Column(sa.Boolean, nullable=False)  # False - male, True - female

    def __str__(self):
        return f"""id: {self.user_id}
full name: {self.full_name}
sex: {self.sex}"""

    def __init__(self, name, sex):
        self.full_name = name
        self.sex = sex
