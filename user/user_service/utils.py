import datetime
import jwt
from django.conf import settings


def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'scope': build_scope(user),
    }
    access_token = jwt.encode(access_token_payload,
        settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow(),
        'scope': build_scope(user),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256')
    return refresh_token


def build_scope(user):
    scope_list = []

    if user.roles.exists():
        for role in user.roles.all():
            scope_list.append("ROLE_" + role.name)
            
    return ' '.join(scope_list)


