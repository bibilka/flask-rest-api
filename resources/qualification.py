from flask_restful import Resource, reqparse, abort
from models.qualification import Qualification
from app import db
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Наименование обязательное поле")


# Класс-ресурс для работы с квалификацией
class QualificationResource(Resource):

    # метод GET для получения информации по квалификации по id
    @jwt_required()
    def get(self, qualification_id):
        return Qualification.serialize(
            Qualification.query.filter_by(id=qualification_id).first_or_404(
                description='Квалификация не найдена'
            )
        )

    # метод PUT для изменения квалификации по id
    @jwt_required()
    def put(self, qualification_id):
        qualification = Qualification.query.filter_by(id=qualification_id).first_or_404(
            description='Квалификация не найдена'
        )
        args = parser.parse_args()
        # валидируем уникальность наименования (исключая текущий объект)
        if Qualification.query.filter_by(name=args['name']).filter(Qualification.id != qualification_id).first():
            abort(422, error='Квалификация с таким названием уже существует')

        # обновляем данные квалификации
        qualification.name = args['name']
        db.session.commit()

        return {'msg': 'Квалификация изменена', 'data': qualification.serialize()}, 200

    # метод DELETE для удаления квалификации по ID
    @jwt_required()
    def delete(self, qualification_id):
        Qualification.query.filter_by(id=qualification_id).first_or_404(
            description='Квалификация не найдена'
        )
        Qualification.query.filter_by(id=qualification_id).delete()
        db.session.commit()
        return {'msg': 'Квалификация удалена'}, 200


# Класс-ресурс для работы со списком квалификаций
class QualificationListResource(Resource):

    # метод GET для получения списка всех квалификаций
    @jwt_required()
    def get(self):
        return [Qualification.serialize(item) for item in Qualification.query.all()]

    # метод POST для создания новой квалификации
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        # валидируем уникальность наименования
        if Qualification.query.filter_by(name=args['name']).first():
            abort(422, error='Такая квалификация уже существует')
        new_qualification = Qualification(name=args['name'])
        # создаем новой квалификации в бд
        db.session.add(new_qualification)
        db.session.commit()
        return {'msg': 'Квалификация успешно добавлена', 'data': new_qualification.serialize()}, 201
