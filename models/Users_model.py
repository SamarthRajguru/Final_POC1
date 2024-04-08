from create_app import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    contact = db.Column(db.BigInteger(), nullable=False)
    role_id = db.Column(db.SmallInteger(), nullable=False)

    def __repr__(self):
        return f"<User name = {self.name}>"


print("Users table created")

# new_user = Users(id=1, name="Sam", email="sama@gmail.com", contact=6263239770)
# print(f"<User name = {new_user.name}>")
