from app import api
from resources.user import UserResource, UserListResource
from resources.speciality import SpecialityResource, SpecialityListResource, SpecialityGroups
from resources.qualification import QualificationResource, QualificationListResource, QualificationGroups
from resources.education_form import EducationFormResource, EducationFormListResource, EducationFormGroups
from resources.group import GroupResource, GroupListResource
from resources import auth

# маршруты для работы с пользователями
api.add_resource(UserListResource, '/api/users', endpoint='users')
api.add_resource(UserResource, '/api/users/<int:user_id>', endpoint='user')

# маршруты для работы со специальностями
api.add_resource(SpecialityListResource, '/api/specialities', endpoint='specialities')
api.add_resource(SpecialityResource, '/api/specialities/<int:speciality_id>', endpoint='speciality')
api.add_resource(SpecialityGroups, '/api/specialities/<int:speciality_id>/groups', endpoint='speciality_groups')

# маршруты для работы с квалификациями
api.add_resource(QualificationListResource, '/api/qualifications', endpoint='qualifications')
api.add_resource(QualificationResource, '/api/qualifications/<int:qualification_id>', endpoint='qualification')
api.add_resource(QualificationGroups, '/api/qualifications/<int:qualification_id>/groups', endpoint='qualification_groups')

# маршруты для работы с формами обучения
api.add_resource(EducationFormListResource, '/api/education_forms', endpoint='education_forms')
api.add_resource(EducationFormResource, '/api/education_forms/<int:education_form_id>', endpoint='education_form')
api.add_resource(EducationFormGroups, '/api/education_forms/<int:education_form_id>/groups', endpoint='education_form_groups')

# маршруты для работы с группами
api.add_resource(GroupListResource, '/api/groups', endpoint='groups')
api.add_resource(GroupResource, '/api/groups/<int:group_id>', endpoint='group')

# маршруты для авторизации JWT
api.add_resource(auth.UserRegistration, '/api/registration')
api.add_resource(auth.UserLogin, '/api/login')
api.add_resource(auth.UserLogoutAccess, '/api/logout/access')
api.add_resource(auth.UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(auth.TokenRefresh, '/api/token/refresh')
