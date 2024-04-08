from flask import Blueprint, request, jsonify
from models.Pets_model import Pets
from create_app import db
import psycopg2
import sqlalchemy

pet_bp = Blueprint("pet", __name__)


@pet_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    id = data.get("id")
    name = data.get("name")
    age = data.get("age")
    breed = data.get("breed")
    location = data.get("location")
    colour = data.get("color")
    description = data.get("description")

    adoption_status = data.get("adoption_status")
    image = data.get("image")

    new_pet = Pets(
        id=id,
        name=name,
        breed=breed,
        age=age,
        description=description,
        image_url="<Paste URL here>",
        adoption_status=adoption_status,
        location=location,
    )

    try:
        print("1")
        db.session.add(new_pet)
        print("2")
        db.session.commit()
        print("3")
        print(f"Pet {new_pet.name} added...")
        return jsonify(f"Pet {new_pet.name} added..."), 200
    except:
        return jsonify({"Error": "Not added"}), 404


#  Retrieve API
@pet_bp.route("/<int:id>", methods=["GET"])
def get_pet(id):
    pet = db.session.query(Pets).filter(pet.id == id).first()

    id = (pet.id,)
    name = (pet.name,)
    breed = (pet.breed,)
    age = (pet.age,)
    description = (pet.description,)
    adoption_status = (pet.adoption_status,)
    location = (pet.location,)

    if pet:
        return (
            jsonify(
                {
                    "id": pet.id,
                    "name": pet.name,
                    "breed": pet.breed,
                    "age": pet.age,
                    "description": pet.description,
                    "adoption_status": pet.adoption_status,
                    "location": pet.location,
                }
            ),
            200,
        )
    return jsonify({"error": "Pet not found"}), 404
