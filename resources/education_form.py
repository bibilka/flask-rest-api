from flask_restful import Resource, reqparse, abort
from models.education_form import EducationForm
from app import db
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Наименование обязательное поле")


# Класс-ресурс для работы с формой обучения
class EducationFormResource(Resource):

    # метод GET для получения информации по квалификации по id
    @jwt_required()
    def get(self, education_form_id):
        return EducationForm.serialize(
            EducationForm.query.filter_by(id=education_form_id).first_or_404(
                description='Форма обучения не найдена'
            )
        )

    # метод PUT для изменения формы обучения по id
    @jwt_required()
    def put(self, education_form_id):
        education_form = EducationForm.query.filter_by(id=education_form_id).first_or_404(
            description='Форма обучения не найдена'
        )
        args = parser.parse_args()
        # валидируем уникальность наименования (исключая текущий объект)
        if EducationForm.query.filter_by(name=args['name']).filter(EducationForm.id != education_form_id).first():
            abort(422, error='Форма обучения с таким названием уже существует')

        # обновляем данные формы обучения
        education_form.name = args['name']
        db.session.commit()

        return {'msg': 'Форма обучения изменена', 'data': education_form.serialize()}, 200

    # метод DELETE для удаления формы обучения по ID
    @jwt_required()
    def delete(self, education_form_id):
        education_form = EducationForm.query.filter_by(id=education_form_id).first_or_404(
            description='Форма обучения не найдена'
        )
        if education_form.groups:
            abort(422,
                  error='Нельзя удалить данную форму обучения, так как она закреплена за одной или несколькими '
                        'группами')
        EducationForm.query.filter_by(id=education_form_id).delete()
        db.session.commit()
        return {'msg': 'Форма обучения удалена'}, 200


# Класс-ресурс для работы со списком форм обучения
class EducationFormListResource(Resource):

    # метод GET для получения списка всех форм обучения
    @jwt_required()
    def get(self):
        return [EducationForm.serialize(item) for item in EducationForm.query.all()]

    # метод POST для создания новой формы обучения
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        # валидируем уникальность наименования
        if EducationForm.query.filter_by(name=args['name']).first():
            abort(422, error='Такая форма обучения уже существует')
        new_education_form = EducationForm(name=args['name'])
        # создаем новой квалификации в бд
        db.session.add(new_education_form)
        db.session.commit()
        return {'msg': 'Форма обучения успешно добавлена', 'data': new_education_form.serialize()}, 201


# Класс-ресурс для получения групп заданной формы обучения
class EducationFormGroups(Resource):

    # метод GET для получения списка групп для специальности по ID
    @jwt_required()
    def get(self, education_form_id):
        education_form = EducationForm.query.filter_by(id=education_form_id).first_or_404(
            description='Форма обучения не найдена'
        )
        return {
            'education_form_id': education_form_id,
            'education_form_name': education_form.name,
            'groups': [group.serialize_for_education_form() for group in education_form.groups]
        }
