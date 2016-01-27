from restaurants import app
from flask import render_template, request
from flask import session as login_session
import crud_functions as crud


@app.context_processor
def inject_restaurants():
    restaurant_list = crud.get_restaurants()
    return dict(restaurant_list=restaurant_list)


@app.context_processor
def login_check():
    if request.args.get('login') == 'true' and app.debug:
        return dict(logged_in=True)
    else:
        if 'username' in login_session:
            return dict(logged_in=True)
        else:
            return dict(logged_in=False)


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
