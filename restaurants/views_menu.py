from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session
import crud_functions as crud
from forms import *


@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def show_menu(restaurant_id):
    menu = crud.get_menu_items(restaurant_id)
    restaurant = crud.get_restaurant(restaurant_id)
    return render_template('/menu/menu.html', menu=menu, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    # Make sure user is logged on first
    if 'username' not in login_session:
        return redirect(url_for('login'))
    form = MenuForm(request.form)
    form.course.choices = [('Appetizer', 'Appetizer'),
                           ('Entree', 'Entree'),
                           ('Beverage', 'Beverage'),
                           ('Dessert', 'Dessert')]
    if request.method == 'POST' and form.validate():
        # Get data from form and then use CRUD function to update
        name = form.name.data
        description = form.description.data
        course = form.course.data
        price = form.price.data
        crud.new_menu_item(name, description, course, price, restaurant_id)
        flash("New Menu Item Created")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    return render_template('/menu/new_menu_item.html', restaurant_id=restaurant_id, form=form)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    # Make sure user is logged on first
    if 'username' not in login_session:
        return redirect(url_for('login'))
    item = crud.get_menu_item(menu_id)
    form = MenuForm(request.form)
    form.course.choices = [('Appetizer', 'Appetizer'),
                           ('Entree', 'Entree'),
                           ('Beverage', 'Beverage'),
                           ('Dessert', 'Dessert')]
    if request.method == 'GET':
        # Set values for form
        form.name.data = item.name
        form.course.data = item.course
        form.description.data = item.description
        form.price.data = item.price
    if request.method == 'POST' and form.validate():
        # Get data from form and then use CRUD function to update
        name = form.name.data
        description = form.description.data
        course = form.course.data
        price = form.price.data
        crud.edit_menu_item(menu_id, name, description, course, price)
        flash("Menu Item Successfully Edited")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    return render_template('/menu/edit_menu_item.html', menu_item=item, restaurant_id=restaurant_id, form=form)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    # Make sure user is logged on first
    if 'username' not in login_session:
        return redirect(url_for('login'))
    if request.method == 'GET':
        item = crud.get_menu_item(menu_id)
        return render_template('/menu/delete_menu_item.html', menu_item=item, restaurant_id=restaurant_id)
    if request.method == 'POST':
        crud.delete_menu_item(menu_id)
        flash("Menu Item Successfully Deleted")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
