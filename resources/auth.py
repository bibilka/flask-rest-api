from flask_restful import Resource, abort, reqparse
from models.user import User
from app import db

parser = reqparse.RequestParser()
parser.add_argument('login', help='Обязательно укажите логин', required=True)
parser.add_argument('password', help='Обязательно укажите пароль', required=True)


# регистрация пользователей
class UserRegistration(Resource):
    def post(self):
        args = parser.parse_args()
        # валидируем уникальность логина
        if User.query.filter_by(login=args['login']).first():
            abort(422, error='Такой пользователь уже существует')
        new_user = User(login=args['login'])
        new_user.set_password(args['password'])
        # создаем нового пользователя в бд
        db.session.add(new_user)
        db.session.commit()
        return {'msg': 'Пользователь успешно добавлен'}, 201


# вход пользователей
class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = User.query.get(data['login'])

        if user and user.check_password(data['password']):
            return True
        else:
            return {'msg': 'Данные неверны'}, 401


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


# обновление токена доступа
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}

