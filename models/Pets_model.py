from create_app import db
from models.Adoption_status import AdoptionStatus


class Pets(db.Model):
    __tablename__ = "pets_details"
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(100))
    breed = db.Column(db.String(100), nullable=False)
    coulor = db.Column(db.String(50))
    age = db.Column(db.Integer())
    description = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    image_url = db.Column(db.String(255))
    adoption_status = db.Column(
        db.Integer(), db.ForeignKey("adoption_status.status_id")
    )
    adoption = db.relationship("AdoptionStatus")

    # category = db.relationship("Category")
    # category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)


new_pet = Pets(
    id=1,
    name="Simba",
    breed="Asiatic",
    age=10,
    description="Simba is a king",
    image_url="<Paste URL here>",
    adoption_status=1,
)

print("Pets table created")
