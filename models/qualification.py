from app import db


# Класс модель - квалификация
class Qualification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # текстовое поле - квалификация подготовки бакалавра (уникальный индекс)
    name = db.Column(db.String(150), index=True, unique=True)

    # метод для сериализации объекта
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
