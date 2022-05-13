from flask_restful import Resource, abort, reqparse
from models.user import User
from models.revoked_token import RevokedToken
from app import db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt

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
        user = User.query.filter_by(login=data['login']).first()

        if user and user.check_password(data['password']):
            # создаем токены
            access_token = create_access_token(identity=data['login'])
            refresh_token = create_refresh_token(identity=data['login'])
            return {
                'msg': 'Авторизация прошла успешно',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'msg': 'Данные неверны'}, 401


# отозвать токен доступа
class UserLogoutAccess(Resource):
    @jwt_required()
    def post(self):
        revoked_token = RevokedToken(jti=get_jwt()['jti'])
        db.session.add(revoked_token)
        db.session.commit()
        return {'msg': 'Токен доступа аннулирован'}


# отозвать refresh токен
class UserLogoutRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        revoked_token = RevokedToken(jti=get_jwt()['jti'])
        db.session.add(revoked_token)
        db.session.commit()
        return {'msg': 'Refresh токен аннулирован'}


# обновление токена доступа
class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}

