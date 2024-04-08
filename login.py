from flask import Blueprint, request, jsonify
from create_app import db, bcrypt
from models.Users_model import Users
from token_generate import generate_JWT_token


login_bp = Blueprint("login_bp", __name__)


@login_bp.route("/", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    print("email: ", email)
    print(db.session.query(Users).filter(Users.email == email).first())

    user_to_be_logged_in = db.session.query(Users).filter(Users.email == email).first()
    print("user_to_be_logged_in: ", user_to_be_logged_in)

    role_id = user_to_be_logged_in.role_id
    print("In Login role_id =", user_to_be_logged_in.role_id)

    if user_to_be_logged_in:

        if bcrypt.check_password_hash(user_to_be_logged_in.password, password):
            access_token = generate_JWT_token(email, role_id)
            print(access_token)
            return (
                jsonify({"Message": "Login Succefull...", "Token": access_token}),
                200,
            )
        else:
            return jsonify({"Message": "Invalid password"}), 401
    else:
        return jsonify({"Message": "User not found"}), 404
