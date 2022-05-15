from flask_restful import Resource, reqparse, abort
from models.speciality import Speciality
from app import db
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Наименование обязательное поле")
parser.add_argument('profile', type=str, required=True, help="Профиль обязательное поле")


# Класс-ресурс для работы со специальностью
class SpecialityResource(Resource):

    # метод GET для получения информации по специальности по id
    @jwt_required()
    def get(self, speciality_id):
        return Speciality.serialize(
            Speciality.query.filter_by(id=speciality_id).first_or_404(
                description='Специальность не найдена'
            )
        )

    # метод PUT для изменения специальности по id
    @jwt_required()
    def put(self, speciality_id):

        speciality = Speciality.query.filter_by(id=speciality_id).first_or_404(
            description='Специальность не найдена'
        )
        args = parser.parse_args()
        # валидируем уникальность профиля (исключая текущий объект)
        if Speciality.query.filter_by(profile=args['profile']).filter(Speciality.id != speciality_id).first():
            abort(422, error='Такой профиль подготовки уже существует')

        # обновляем данные специальности
        speciality.name = args['name']
        speciality.profile = args['profile']
        db.session.commit()

        return {'msg': 'Специальность изменена', 'data': speciality.serialize()}, 200

    # метод DELETE для удаления специальности по ID
    @jwt_required()
    def delete(self, speciality_id):
        speciality = Speciality.query.filter_by(id=speciality_id).first_or_404(
            description='Специальность не найдена'
        )
        if speciality.groups:
            abort(422, error='Нельзя удалить данную специальность, так как она закреплена за одной или несколькими '
                             'группами')

        Speciality.query.filter_by(id=speciality_id).delete()
        db.session.commit()
        return {'msg': 'Специальность удалена'}, 200


# Класс-ресурс для работы со списком специальностей
class SpecialityListResource(Resource):

    # метод GET для получения списка всех специальностей
    @jwt_required()
    def get(self):
        return [Speciality.serialize(item) for item in Speciality.query.all()]

    # метод POST для создания новой специальности
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        # валидируем уникальность профиля (исключая текущий объект)
        if Speciality.query.filter_by(profile=args['profile']).first():
            abort(422, error='Такой профиль подготовки уже существует')
        new_spec = Speciality(name=args['name'], profile=args['profile'])
        # создаем новой специальности в бд
        db.session.add(new_spec)
        db.session.commit()
        return {'msg': 'Специальность успешно добавлена', 'data': new_spec.serialize()}, 201


# Класс-ресурс для получения групп заданной специальности
class SpecialityGroups(Resource):

    # метод GET для получения списка групп для специальности по ID
    @jwt_required()
    def get(self, speciality_id):
        speciality = Speciality.query.filter_by(id=speciality_id).first_or_404(
            description='Специальность не найдена'
        )
        return {
            'speciality_id': speciality_id,
            'speciality_name': speciality.name,
            'groups': [group.serialize_for_speciality() for group in speciality.groups]
        }
