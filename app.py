from create_app import app
from users_routes.create_users import create_user_bp
from users_routes.retrive_user import retrive_user_bp
from users_routes.update_user import update_user_bp
from users_routes.delete_user import delete_user_bp
from login import login_bp
from pet_routes.create_pet import pet_bp


from category_routes.category_routes import category_bp

app.register_blueprint(create_user_bp, url_prefix="/create")

app.register_blueprint(retrive_user_bp, url_prefix="/retrive")

app.register_blueprint(delete_user_bp, url_prefix="/delete")

app.register_blueprint(login_bp, url_prefix="/login")

app.register_blueprint(category_bp, url_prefix="/category")

app.register_blueprint(pet_bp, url_prefix="/pet")


if __name__ == "__main__":
    app.run(debug=True)
