from restaurants import app
from wtforms import SelectField, StringField, validators
from flask_wtf.file import FileField, FileAllowed
from flask_wtf.form import Form


class RestaurantForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    image = FileField('Image', validators=[FileAllowed(app.config.get('ALLOWED_EXTENSIONS'), 'Images only!')])


class MenuForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    course = SelectField('Course', [validators.DataRequired()])
    price = StringField('Price', [validators.DataRequired()])
