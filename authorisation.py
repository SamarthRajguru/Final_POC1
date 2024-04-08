from flask import request, jsonify
from functools import wraps
from create_app import app
import jwt


def role_required(role_id):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if token:
                try:
                    token = token.split(" ")[1]
                    payload = jwt.decode(
                        token, app.config["SECRET_KEY"], algorithms=["HS256"]
                    )
                    user_role = str(payload.get("role_id"))
                    print("user_rolee", type(user_role), user_role)
                    print("as", user_role)
                    print("role_id", type(role_id), role_id)
                    if user_role == role_id:
                        return func(*args, **kwargs)
                    else:
                        return jsonify({"error": "insufficient permission"})
                except jwt.ExpiredSignatureError:
                    return jsonify({"error": "Token has expired"}), 401
                except jwt.InvalidTokenError:
                    return jsonify({"error": "Token is invalid"}), 401
            else:
                return jsonify({"error": "Token is missing"}), 401

        return wrapper

    return decorator
