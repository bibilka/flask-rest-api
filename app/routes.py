from app import api
from resources.user import UserResource, UserListResource
from resources.speciality import SpecialityResource, SpecialityListResource
from resources import auth

# маршруты для работы с пользователями
api.add_resource(UserListResource, '/api/users', endpoint='users')
api.add_resource(UserResource, '/api/users/<int:user_id>', endpoint='user')

# маршруты для работы с пользователями
api.add_resource(SpecialityListResource, '/api/specialities', endpoint='specialities')
api.add_resource(SpecialityResource, '/api/specialities/<int:speciality_id>', endpoint='speciality')

# маршруты для авторизации JWT
api.add_resource(auth.UserRegistration, '/api/registration')
api.add_resource(auth.UserLogin, '/api/login')
api.add_resource(auth.UserLogoutAccess, '/api/logout/access')
api.add_resource(auth.UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(auth.TokenRefresh, '/api/token/refresh')