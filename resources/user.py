from flask_restful import Resource
from models.user import User
from flask_jwt_extended import jwt_required


# Класс-ресурс для работы с пользователем
class UserResource(Resource):

    # метод GET для получения информации по пользователю по id
    @jwt_required()
    def get(self, user_id):
        return User.serialize(
            User.query.filter_by(id=user_id).first_or_404(
                description='Пользователь не найден'
            )
        )


# Класс-ресурс для работы со списком пользователей
class UserListResource(Resource):

    # метод GET для получения списка всех пользователей
    @jwt_required()
    def get(self):
        users = User.query.all()
        return [User.serialize(item) for item in users]
