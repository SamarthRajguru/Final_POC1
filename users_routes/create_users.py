from flask import Blueprint, request, jsonify
from models.Users_model import Users
from create_app import db, bcrypt
import sqlalchemy.exc
import psycopg2.errors
from authentication import token_required
from authorisation import role_required


create_user_bp = Blueprint("create_user_bp", __name__)


@create_user_bp.route("/user", methods=["POST"])
@token_required
@role_required("1")
def create_user():
    data = request.get_json()
    local_email = data.get("email")
    local_password = data.get("password")
    local_name = data.get("name")
    local_contact = data.get("contact")
    role_id = data.get("role_id")
    hashed_password = bcrypt.generate_password_hash(local_password).decode("utf-8")

    new_user = Users(
        email=local_email,
        password=hashed_password,
        name=local_name,
        contact=local_contact,
        role_id=role_id,
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        print(f"User {new_user.name} added...")
        return jsonify(f"User {new_user.name} added...")
    except psycopg2.errors.UniqueViolation:
        return jsonify({"Error": "Unique Voilation"})
    except sqlalchemy.exc.IntegrityError as err:
        print(err)
        e = {"Error": print(err)}
        return jsonify({"Error": "Integrity Error due to redundancy"}), 404
