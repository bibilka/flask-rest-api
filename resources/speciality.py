from flask_restful import Resource, reqparse, abort
from models.speciality import Speciality
from app import db


# Класс-ресурс для работы со специальностью
class SpecialityResource(Resource):

    # метод GET для получения информации по специальности по id
    def get(self, speciality_id):
        return Speciality.serialize(
            Speciality.query.filter_by(id=speciality_id).first_or_404(
                description='Специальность не найдена'
            )
        )


# Класс-ресурс для работы со списком специальностей
class SpecialityListResource(Resource):

    # метод GET для получения списка всех специальностей
    def get(self):
        return [Speciality.serialize(item) for item in Speciality.query.all()]

    # метод POST для создания новой специальности
    def post(self):
        parser = reqparse.RequestParser()
        # валидируем данные
        parser.add_argument('name', type=str, required=True, help="Наименование обязательное поле")
        parser.add_argument('profile', type=str, required=True, help="Профиль обязательное поле")
        args = parser.parse_args()
        # валидируем уникальность наименования
        if Speciality.query.filter_by(name=args['name']).first():
            abort(422, error='Такая специальность уже существует')
        new_spec = Speciality(name=args['name'], profile=args['profile'])
        # создаем новой специальности в бд
        db.session.add(new_spec)
        db.session.commit()
        return {'msg': 'Специальность успешно добавлена'}, 201