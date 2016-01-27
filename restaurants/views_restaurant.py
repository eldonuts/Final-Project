from restaurants import app
from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session
import crud_functions as crud
from forms import *


@app.route('/restaurants')
@app.route('/')
def show_restaurants():
    restaurants = crud.get_restaurants()
    return render_template('/restaurants/restaurants.html', restaurants=restaurants)


@app.route('/restaurant/new', methods=['GET', 'POST'])
def new_restaurant():
    if 'username' not in login_session:
        return redirect(url_for('login'))
    form = RestaurantForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        address = form.address.data

        image = form.image.data
        if image:
            image_ext = image.filename.rsplit('.', 1)[1]
            allowed_ext = app.config.get('ALLOWED_EXTENSIONS')
            if image_ext in allowed_ext:
                crud.new_restaurant(name, description, address, image)
            else:
                flash("Couldn't update image, must be in: " + str(allowed_ext))
        else:
            crud.new_restaurant(name, description, address)

        flash("New Restaurant Created")
        return redirect(url_for('show_restaurants'))
    return render_template('/restaurants/new_restaurant.html', form=form)


@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    if 'username' not in login_session:
        return redirect(url_for('login'))
    form = RestaurantForm()
    restaurant = crud.get_restaurant(restaurant_id)
    if request.method == 'GET':
        # Set default values
        form.name.data = restaurant.name
        form.description.data = restaurant.description
        form.address.data = restaurant.address
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        address = form.address.data
        image = form.image.data
        crud.edit_restaurant(restaurant_id, name, description, address, image)
        flash("Restaurant Successfully Edited")
        return redirect(url_for('show_restaurants'))
    return render_template('/restaurants/edit_restaurant.html', restaurant=restaurant, form=form)


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    if 'username' not in login_session:
        return redirect(url_for('login'))
    if request.method == 'GET':
        restaurant = crud.get_restaurant(restaurant_id)
        return render_template('/restaurants/delete_restaurant.html', restaurant=restaurant)
    if request.method == 'POST':
        crud.delete_restaurant(restaurant_id)
        flash("Restaurant Successfully Deleted")
        return redirect(url_for('show_restaurants'))
