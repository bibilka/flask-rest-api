from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
# from flask_jwt_extended import JWTManager
from config import Config

# инициализируем приложение, и объект для реализации rest api, и подключаем конфигурацию
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# создаем объекты для работы с базой данных и для миграций
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# jwt
# jwt = JWTManager(app)

# подключаем обработчик ошибок и файл с роутами
from app import handler, routes
from models.user import User
from models.speciality import Speciality
from models.qualification import Qualification
from models.education_form import EducationForm
from models.group import Group
