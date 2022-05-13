from app import api
from resources.user import UserResource, UserListResource
from resources.speciality import SpecialityResource, SpecialityListResource
from resources.qualification import QualificationResource, QualificationListResource
from resources.education_form import EducationFormResource, EducationFormListResource
from resources import auth

# маршруты для работы с пользователями
api.add_resource(UserListResource, '/api/users', endpoint='users')
api.add_resource(UserResource, '/api/users/<int:user_id>', endpoint='user')

# маршруты для работы со специальностями
api.add_resource(SpecialityListResource, '/api/specialities', endpoint='specialities')
api.add_resource(SpecialityResource, '/api/specialities/<int:speciality_id>', endpoint='speciality')

# маршруты для работы с квалификациями
api.add_resource(QualificationListResource, '/api/qualifications', endpoint='qualifications')
api.add_resource(QualificationResource, '/api/qualifications/<int:qualification_id>', endpoint='qualification')

# маршруты для работы с формами обучения
api.add_resource(EducationFormListResource, '/api/education_forms', endpoint='education_forms')
api.add_resource(EducationFormResource, '/api/education_forms/<int:education_form_id>', endpoint='education_form')

# маршруты для авторизации JWT
api.add_resource(auth.UserRegistration, '/api/registration')
api.add_resource(auth.UserLogin, '/api/login')
api.add_resource(auth.UserLogoutAccess, '/api/logout/access')
api.add_resource(auth.UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(auth.TokenRefresh, '/api/token/refresh')
