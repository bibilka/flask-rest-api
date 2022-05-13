from app import db
from werkzeug.security import generate_password_hash, check_password_hash


# модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # логин - текстовое поле с уникальным индексолм
    login = db.Column(db.String(64), index=True, unique=True)
    # пароль - текстовое поле
    password = db.Column(db.String(128))

    # сериализация объекта
    def serialize(self):
        return {
            'id': self.id,
            'login': self.login
        }

    # метод для сохранения пароля для пользователя (в виде хэша)
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # метод для проверки пароля на совпадение
    def check_password(self, password):
        return check_password_hash(self.password, password)
