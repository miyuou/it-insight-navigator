from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import abort

def role_required(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get('role') not in roles:
                abort(403, description="Accès interdit : rôle insuffisant")
            return fn(*args, **kwargs)
        return wrapper
    return decorator 