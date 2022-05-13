from app import db


# Класс модель - Студенческая группа
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # текстовое поле - наименование группы (уникальный индекс)
    name = db.Column(db.String(150), index=True, unique=True)
    # текстовое поле - факультет
    faculty = db.Column(db.String(150))
    # номер курса - число
    course = db.Column(db.Integer)
    # количество студентов - число
    students_count = db.Column(db.Integer)
    # Количество подгрупп - число
    subgroups_count = db.Column(db.Integer)

    # специальность
    speciality_id = db.Column(db.Integer, db.ForeignKey('speciality.id'))
    speciality = db.relationship("Speciality", backref='speciality')

    # квалификация
    qualification_id = db.Column(db.Integer, db.ForeignKey('qualification.id'))
    qualification = db.relationship("Qualification", backref='qualification')

    # специальность
    education_form_id = db.Column(db.Integer, db.ForeignKey('education_form.id'))
    education_form = db.relationship("EducationForm", backref='education_form')

    # метод для сериализации объекта
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'profile': self.profile
        }
