import psycopg2
from create_app import app, db
from models.Users_model import Users
from models.Categories_model import Category
from models.Pets_model import Pets
from models.Role_model import Role

with app.app_context():
    db.create_all()
    db.session.commit()
    print("All Tables created")
