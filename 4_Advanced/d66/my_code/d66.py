# Café & Wifi REST API

import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


def to_dict(random_cafe):
    dictionary = {}
    # Loop through each column in the data record
    for column in random_cafe.__table__.columns:
        # Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(random_cafe, column.name)
    return dictionary


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result=db.session.execute(db.select(Cafe))
    all_cafes=result.scalars().all()
    random_cafe=random.choice(all_cafes)
    return jsonify(cafe=to_dict(random_cafe))

@app.route("/all")
def all_cafe():
    result=db.session.execute(db.select(Cafe))
    all_cafes=result.scalars().all()
    return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])

@app.route("/search")
def search_cafe():
    cafe_loc=request.args.get('loc').title()
    result=db.session.execute(db.select(Cafe).where(Cafe.location==cafe_loc))
    all_cafes=result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])
    else:
        return jsonify(error={
            'Not Found':'Sorry, we dont have a cafe at that location'
        })


# HTTP POST - Create Record

@app.route("/add",methods=["POST"])
def add_cafe():
    api_key = request.args.get('api-key')
    if api_key == "TopSecretAPIKey":
        new_cafe=Cafe(
            name=str(request.form.get('name')),
            map_url=str(request.form.get('map_url')),
            img_url=str(request.form.get('img_url')),
            location=str(request.form.get('location')),
            seats=str(request.form.get('seats')),
            has_toilet=bool(int(request.form.get('has_toilet'))),
            has_wifi=bool(int(request.form.get('has_wifi'))),
            has_sockets=bool(int(request.form.get('has_sockets'))),
            can_take_calls=bool(int(request.form.get('can_take_calls'))),
            coffee_price=str(request.form.get('coffee_price')),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={'Success':'Successfully added new Cafe'})
    else:
        return jsonify(error={'Not Found': "Sorry, That's not allowed, make sure you have a correct api_key"}), 403

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>",methods=['PATCH'])
def update_cafe(cafe_id):
    new_price=request.args.get('new_price')
    cafe=db.session.get(entity=Cafe,ident=cafe_id)
    if cafe:
        cafe.coffee_price=new_price
        db.session.commit()
        return jsonify(Success='Successfully updated the price')
    else:
        return jsonify(error={'Not Found': 'Sorry, a cafe with that id was not found in database'}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>",methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key=request.args.get('api-key')
    if api_key=="TopSecretAPIKey":
        cafe = db.session.get(entity=Cafe, ident=cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(Success='Successfully Deleted cafe')
        else:
            return jsonify(error={'Not Found': 'Sorry, a cafe with that id was not found in database'}), 404
    else:
        return jsonify(error={'Not Found': "Sorry, That's not allowed, make sure you have a correct api_key"}), 403

if __name__ == '__main__':
    app.run(debug=True)
