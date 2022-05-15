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
    speciality = db.relationship("Speciality", back_populates="groups")

    # квалификация
    qualification_id = db.Column(db.Integer, db.ForeignKey('qualification.id'))
    qualification = db.relationship("Qualification", back_populates="groups")

    # специальность
    education_form_id = db.Column(db.Integer, db.ForeignKey('education_form.id'))
    education_form = db.relationship("EducationForm", back_populates="groups")

    # метод для сериализации объекта
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'course': self.course,
            'students_count': self.students_count,
            'subgroups_count': self.subgroups_count,
            'speciality': self.speciality.serialize(),
            'qualification': self.qualification.serialize(),
            'education_form': self.education_form.serialize()
        }

    # сериализация группы для запроса в специальности
    def serialize_for_speciality(self):
        return {
            'id': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'course': self.course,
            'students_count': self.students_count,
            'subgroups_count': self.subgroups_count,
            'qualification': self.qualification.serialize(),
            'education_form': self.education_form.serialize()
        }

    # сериализация группы для запроса в квалификацияя
    def serialize_for_qualification(self):
        return {
            'id': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'course': self.course,
            'students_count': self.students_count,
            'subgroups_count': self.subgroups_count,
            'speciality': self.speciality.serialize(),
            'education_form': self.education_form.serialize()
        }

    # сериализация группы для запроса в форме обучения
    def serialize_for_education_form(self):
        return {
            'id': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'course': self.course,
            'students_count': self.students_count,
            'subgroups_count': self.subgroups_count,
            'speciality': self.speciality.serialize(),
            'qualification': self.qualification.serialize(),
        }
