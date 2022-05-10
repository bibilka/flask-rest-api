from flask_restful import Resource, reqparse, abort
from models.user import User
from app import db

class UserResource(Resource):
    def get(self, user_id):
        return User.serialize(
            User.query.filter_by(id=user_id).first_or_404(
                description='Пользователь не найден'
            )
        )


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [User.serialize(item) for item in users]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str, required=True, help="Логин обязательное поле")
        parser.add_argument('password', type=str, required=True, help='Пароль обязательное поле')
        args = parser.parse_args()
        if User.query.filter_by(login=args['login']).first():
            abort(422, error='Такой пользователь уже существует')
        new_user = User(login=args['login'])
        new_user.set_password(args['password'])
        db.session.add(new_user)
        db.session.commit()
        return {'msg': 'Пользователь успешно добавлен'}, 201