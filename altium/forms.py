from wtforms import  StringField, validators
from wtforms.widgets import PasswordInput 
from flask_wtf import FlaskForm as Form
from . import models
from . import util

def create_component_form(model):
    dct = {}
    for key in model.properties:
        if key not in models.HIDDEN_FIELDS:
            dct[key] = StringField(util.prettify(key), id='id_%s' % key)
    return type('ComponentForm', (Form,), dct)

class PrefsForm(Form):
    ALTIUM_SVN_URL = StringField('SVN URL', validators=[validators.DataRequired()])
    ALTIUM_SVN_USER = StringField('SVN Username')
    ALTIUM_SVN_PASS = StringField('SVN Password', widget=PasswordInput(hide_value=False)) #I'm a bad person
    ALTIUM_SYM_PATH = StringField('SchLib Path', validators=[validators.DataRequired()])
    ALTIUM_FTPT_PATH = StringField('PcbLib Path', validators=[validators.DataRequired()])
    
    SQLALCHEMY_DATABASE_URI = StringField('Database URI', validators=[validators.DataRequired()])
    
def create_prefs_form():
    from altium import app
    return PrefsForm(obj=util.AttributeWrapper(app.config))
