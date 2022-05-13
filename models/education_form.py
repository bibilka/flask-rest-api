from app import db


# Класс модель - Форма обучения
class EducationForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # текстовое поле - форма обучения (уникальный индекс)
    name = db.Column(db.String(150), index=True, unique=True)

    # метод для сериализации объекта
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
