from restaurants import app
from flask import render_template, request
from flask import session as login_session
import crud_functions as crud


@app.context_processor
def inject_restaurants():
    """This context processor injects the list of restaurants
    into each app.route so that it can be used for the navigation
    menu
    """
    restaurant_list = crud.get_restaurants()
    return dict(restaurant_list=restaurant_list)


@app.context_processor
def login_check():
    """This context processor injects a logged_in variable
    that is calculated based on if the user is logged in.
    It also adds the option to use ?login=true on URIs to
    fake a login (only if DEBUG is enabled).
    """
    if request.args.get('login') == 'true' and app.debug:
        return dict(logged_in=True)
    else:
        if 'username' in login_session:
            return dict(logged_in=True)
        else:
            return dict(logged_in=False)


@app.after_request
def add_header(response):
    """Used to disable caching so that when images are
    updated, the change on the page properly.
    """
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

