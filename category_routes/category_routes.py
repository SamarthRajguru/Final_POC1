from flask import Blueprint, request, jsonify
from models.Categories_model import Category
from create_app import db
import sqlalchemy.exc
from psycopg2.errors import NotNullViolation


category_bp = Blueprint("create_category", __name__)


@category_bp.route("/create", methods=["POST"])
def create_category():
    data = request.get_json()
    category_id = data.get("id")
    category_name = data.get("category_name")

    new_category = Category(id=category_id, name=category_name)

    try:
        print("1")
        db.session.add(new_category)
        print("2")
        db.session.commit()
        print("3")
        return jsonify(f"Category {new_category.name} added..."), 200
    except NotNullViolation as err:
        print(err)
        e = {"Error": print(err)}
        return jsonify({"Error": "NotNullViolation"}), 404
    except sqlalchemy.exc.SQLAlchemyError as err:
        print(err)
        e = {"Error": print(err)}
        return jsonify({"Error": "SQLAlchemyError"}), 500


@category_bp.route("retrive/<int:category_id>", methods=["GET"])
def retrieve_category(category_id):
    category = Category.query.get(category_id)
    print(category)
    id = category.id
    name = category.name
    print(id, name)
    if category:
        return jsonify({"CategoryID": id, "Category": name}), 200
    else:
        return jsonify({"Error": "Category not found"}), 404


@category_bp.route("update/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    category = Category.query.get(category_id)
    if category:
        data = request.get_json()
        new_name = data.get("category_name")
        if new_name:
            category.name = new_name
            try:
                db.session.commit()
                return jsonify(f"Category {category.name} updated..."), 200
            except sqlalchemy.exc.SQLAlchemyError as err:
                print(err)
                return jsonify({"Error": "Failed to update category"}), 500
        else:
            return jsonify({"Error": "Invalid data provided"}), 400
    else:
        return jsonify({"Error": "Category not found"}), 404


@category_bp.route("/delete/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if category:
        try:
            db.session.delete(category)
            db.session.commit()
            return jsonify(f"Category {category.name} deleted..."), 200
        except sqlalchemy.exc.SQLAlchemyError as err:
            print(err)
            return jsonify({"Error": "Failed to delete category"}), 500
    else:
        return jsonify({"Error": "Category not found"}), 404
