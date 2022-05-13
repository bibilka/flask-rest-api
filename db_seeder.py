from app import db
from models.speciality import Speciality
from models.user import User
from models.qualification import Qualification
from models.education_form import EducationForm

user = User(login="user")
user.set_password("password")
db.session.add(user)

db.session.add(
    Speciality(name="Информатика и вычислительная техника", profile="Теоретические основы информатики")
)
db.session.add(
    Speciality(name="Информатика и вычислительная техника", profile="Математическое моделирование, численные методы и комплексы программ")
)
db.session.add(
    Speciality(name="Экономика", profile="Бухгалтерский учет, статистика")
)

db.session.add(
    Qualification(name="Бакалавриат")
)
db.session.add(
    Qualification(name="Специалитет")
)

db.session.add(
    EducationForm(name="Очная")
)
db.session.add(
    EducationForm(name="Заочная")
)
db.session.add(
    EducationForm(name="Очно-заочная")
)

db.session.commit()
