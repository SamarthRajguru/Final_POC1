from flask import Blueprint, request, jsonify
from models.Users_model import Users
from create_app import db, bcrypt
from authentication import token_required
from authorisation import role_required

update_user_bp = Blueprint("update_user_bp", __name__)


@update_user_bp.route("/", methods=["PUT"])
@token_required
@role_required("1")
def update():
    data = request.get_json()
    id = data.get("id")
    user = db.session.query(Users).filter(Users.id == id).first()

    email = ""
    name = ""
    contact = ""
    password = ""

    if user:
        if not data.get("email"):
            email = user.email
        else:
            email = data.get("email")

        if not data.get("name"):
            name = user.name
        else:
            name = data.get("name")

        if not data.get("contact"):
            contact = user.contact
        else:
            contact = data.get("contact")

        if not data.get("role_id"):
            role_id = user.role_id
        else:
            role_id = data.get("role_id")

        password = data.get("password")

        user.name = name
        user.email = email
        user.contact = contact
        user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        user.role_id = role_id

        db.session.commit()

        return jsonify({"Message": "User " + user.name + " updated successfully..."})
    else:
        return jsonify({"Message": "User not found"}), 404
