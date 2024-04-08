from flask import Blueprint, request, jsonify
from models.Users_model import Users
from create_app import db
from authentication import token_required
from authorisation import role_required

delete_user_bp = Blueprint("delete_user_bp", __name__)


@delete_user_bp.route("/", methods=["DELETE"])
@token_required
@role_required("1")
def delete():
    data = request.get_json()
    id = data.get("id")

    user = db.session.query(Users).filter(Users.id == id).first()

    if user:

        name = user.name
        db.session.delete(user)
        db.session.commit()

        return jsonify({"Message": "User " + name + " deleted successfully..."})
    else:
        return jsonify({"Message": "User not found"}), 404
