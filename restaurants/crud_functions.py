import os
from restaurants.models import *
from werkzeug.utils import secure_filename
from flask import flash
from sqlalchemy import exc


# Restaurant Functions

def get_restaurants():
    return db.session.query(Restaurant).all()


def get_restaurant(restaurant_id):
    return db.session.query(Restaurant).filter(Restaurant.id == restaurant_id).one()


def new_restaurant(name, description, address, image=None):
    restaurant = Restaurant(name=name, description=description, address=address)
    db.session.add(restaurant)
    db.session.commit()
    if image:
        upload_restaurant_image(image, restaurant.id)


def edit_restaurant(restaurant_id, name, description, address, image=None):
    restaurant = get_restaurant(restaurant_id)
    restaurant.name = name
    restaurant.description = description
    restaurant.address = address
    db.session.commit()
    if image:
        upload_restaurant_image(image, restaurant_id)


def delete_restaurant(restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    db.session.delete(restaurant)
    db.session.commit()


def upload_restaurant_image(image, restaurant_id):
    image_ext = image.filename.rsplit('.', 1)[1]
    allowed_ext = app.config.get('ALLOWED_EXTENSIONS')
    if image_ext in allowed_ext:
        filename = secure_filename(str(restaurant_id) + '.jpg')
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        restaurant = get_restaurant(restaurant_id)
        restaurant.img = '/static/restaurant_images/' + filename
        db.session.commit()
    else:
        flash("Couldn't update image, must be in: " + str(allowed_ext))


# Menu Functions

def get_menu_items(restaurant_id):
    return db.session.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).all()


def get_menu_item(menu_item_id):
    return db.session.query(MenuItem).filter(MenuItem.id == menu_item_id).one()


def new_menu_item(name, description, course, price, restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    item = MenuItem(name=name, description=description, course=course, price=price, restaurant=restaurant)
    db.session.add(item)
    db.session.commit()


def edit_menu_item(menu_item_id, name, description, course, price):
    item = get_menu_item(menu_item_id)
    item.name = name
    item.description = description
    item.course = course
    item.price = price
    db.session.commit()


def delete_menu_item(menu_item_id):
    item = get_menu_item(menu_item_id)
    db.session.delete(item)
    db.session.commit()


def new_user(login_session):
    user_new = Users(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    db.session.add(user_new)
    db.session.commit()
    user = db.session.query(Users).filter_by(email=login_session['email']).one()
    return user.id


def get_user_info(user_id):
    user = db.session.query(Users).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    try:
        user = db.session.query(Users).filter_by(email=email).one()
        return user.id
    except exc.SQLAlchemyError:
        return None
