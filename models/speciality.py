from app import db


# Класс модель - специальность (направление подготовки)
class Speciality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # текстовое поле - направление подготовки бакалавра (уникальный индекс)
    name = db.Column(db.String(150), index=True, unique=True)
    # текстовое поле - профиль подготовки
    profile = db.Column(db.String(150))

    # метод для сериализации объекта
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'profile': self.profile
        }
