import jwt
from datetime import datetime, timedelta
from create_app import app


def generate_JWT_token(email, role_id):
    expiration_time = datetime.now() + timedelta(days=1)
    payload = {"email": email, "role_id": role_id, "exp": expiration_time}
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
    return token
