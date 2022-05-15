from app import db


# Класс модель - специальность (направление подготовки)
class Speciality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # текстовое поле - направление подготовки бакалавра
    name = db.Column(db.String(150))
    # текстовое поле - профиль подготовки (уникальный индекс)
    profile = db.Column(db.String(150), index=True, unique=True)

    # связь с группами
    groups = db.relationship("Group", back_populates="speciality")

    # метод для сериализации объекта
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'profile': self.profile
        }
