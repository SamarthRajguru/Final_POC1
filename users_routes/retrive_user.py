from flask import Blueprint, request, jsonify
from models.Users_model import Users
from create_app import db
from authentication import token_required
from authorisation import role_required

retrive_user_bp = Blueprint("retrive_user_bp", __name__)


@retrive_user_bp.route("/users", methods=["GET"])
@token_required
@role_required("1")
def retrive_all():
    list = db.session.query(Users).all()
    print("This is list...", list)
    users_list = [
        {"id": user.id, "name": user.name, "email": user.email} for user in list
    ]
    return jsonify(users_list)


@retrive_user_bp.route("/user", methods=["GET"])
@token_required
# @role_required("1")
def retrive_one():
    data = request.get_json()

    user = db.session.query(Users).filter(Users.id == data.get("id")).first()
    print(data.get("id"))
    if user:
        print("This is User", user)
        users_list = [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "contact": user.contact,
                "role": user.role_id,
            }
        ]
        return jsonify(users_list)
    else:
        return jsonify({"Message": "User not found"})
