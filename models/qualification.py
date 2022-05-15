from app import db


# Класс модель - квалификация
class Qualification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # текстовое поле - квалификация подготовки бакалавра (уникальный индекс)
    name = db.Column(db.String(150), index=True, unique=True)

    # связь с группами
    groups = db.relationship("Group", back_populates="qualification")

    # метод для сериализации объекта
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
