from app import api
from resources.user import UserResource, UserListResource

api.add_resource(UserListResource, '/api/users', endpoint='users')
api.add_resource(UserResource, '/api/users/<int:user_id>', endpoint='user')
