from restaurants import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Restaurant(db.Model):

    __tablename__ = 'restaurant'

    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    address = db.Column(db.String(250))
    img = db.Column(db.String(500))

    @property
    def serialize(self):
        """Serialize property used for API calls"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'address': self.address,
        }


class MenuItem(db.Model):

    __tablename__ = 'menu_item'

    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(25))
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
