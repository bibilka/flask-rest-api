from flask_restful import Resource, reqparse, abort
from models.group import Group
from models.speciality import Speciality
from models.qualification import Qualification
from models.education_form import EducationForm
from app import db
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Наименование обязательное поле")
parser.add_argument('faculty', type=str, required=True, help="Факультет обязательное поле")
parser.add_argument('course', type=int, required=True, help="Номер курса обязательное поле")
parser.add_argument('students_count', type=int, required=True, help="Количество студентов обязательное поле")
parser.add_argument('subgroups_count', type=int, required=True, help="Количество подгрупп обязательное поле")
parser.add_argument('speciality_id', type=int, required=True, help="ID специальности обязательное поле")
parser.add_argument('qualification_id', type=int, required=True, help="ID квалификации обязательное поле")
parser.add_argument('education_form_id', type=int, required=True, help="ID формы обучения обязательное поле")


# Класс-ресурс для работы с группой
class GroupResource(Resource):

    # метод GET для получения информации по группе по id
    @jwt_required()
    def get(self, group_id):
        return Group.serialize(
            Group.query.filter_by(id=group_id).first_or_404(
                description='Группа не найдена'
            )
        )

    # метод PUT для изменения группы по id
    @jwt_required()
    def put(self, group_id):
        args = parser.parse_args()

        # проверяем существование группы, специальности, квалификации и формы обучения
        group = Group.query.filter_by(id=group_id).first_or_404(
            description='Группа не найдена')
        Speciality.query.filter_by(id=args['speciality_id']).first_or_404(
            description='Специальность ID=' + str(args['speciality_id']) + ' не найдена')
        Qualification.query.filter_by(id=args['qualification_id']).first_or_404(
            description='Квалификация ID=' + str(args['qualification_id']) + ' не найдена')
        EducationForm.query.filter_by(id=args['education_form_id']).first_or_404(
            description='Форма обучения ID=' + str(args['education_form_id']) + ' не найдена')

        # валидируем уникальность наименования (исключая текущий объект)
        if Group.query.filter_by(name=args['name']).filter(Group.id != group_id).first():
            abort(422, error='Группа с таким названием уже существует')

        # обновляем данные группы
        group.name = args['name']
        group.faculty = args['faculty']
        group.course = args['course']
        group.students_count = args['students_count']
        group.subgroups_count = args['subgroups_count']
        group.speciality_id = args['speciality_id']
        group.qualification_id = args['qualification_id']
        group.education_form_id = args['education_form_id']
        db.session.commit()

        return {'msg': 'Группа изменена', 'data': group.serialize()}, 200

    # метод DELETE для удаления группы по ID
    @jwt_required()
    def delete(self, group_id):
        Group.query.filter_by(id=group_id).first_or_404(
            description='Группа не найдена'
        )
        Group.query.filter_by(id=group_id).delete()
        db.session.commit()
        return {'msg': 'Группа удалена'}, 200


# Класс-ресурс для работы со списком групп
class GroupListResource(Resource):

    # метод GET для получения списка всех групп
    @jwt_required()
    def get(self):
        return [Group.serialize(item) for item in Group.query.all()]

    # метод POST для создания новой квалификации
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        # проверяем существование специальности, квалификации и формы обучения
        Speciality.query.filter_by(id=args['speciality_id']).first_or_404(
            description='Специальность ID=' + str(args['speciality_id']) + ' не найдена')
        Qualification.query.filter_by(id=args['qualification_id']).first_or_404(
            description='Квалификация ID=' + str(args['qualification_id']) + ' не найдена')
        EducationForm.query.filter_by(id=args['education_form_id']).first_or_404(
            description='Форма обучения ID=' + str(args['education_form_id']) + ' не найдена')
        # валидируем уникальность наименования
        if Group.query.filter_by(name=args['name']).first():
            abort(422, error='Такая группа уже существует')
        new_group = Group(name=args['name'], faculty=args['faculty'], course=args['course'],
                          students_count=args['students_count'], subgroups_count=args['subgroups_count'],
                          speciality_id=args['speciality_id'], qualification_id=args['qualification_id'],
                          education_form_id=args['education_form_id'])
        # создаем новой группы в бд
        db.session.add(new_group)
        db.session.commit()
        return {'msg': 'Группа успешно добавлена', 'data': new_group.serialize()}, 201
