from flask_login import login_required
from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from ..services.user_service import current_user_repr
from ..services.postgress_service import get_users_and_privs

from ..forms import PostgresqlTestForm


home = Blueprint('home', __name__)

# Synchronous   
@home.route('/', methods=['GET'])
@login_required
def homepage():
        
    responsebody = current_user_repr()
    user_rep = responsebody['payload']

    test_form = PostgresqlTestForm()
    
    return render_template(template_name_or_list='homepage.html', 
                           user=user_rep,
                           test_form=test_form,
                           userdata=None
                           )
# Synchronous           
@home.route('/get_postgress_users', methods=['POST'])
@login_required
def get_postgress_users():
    test_form  = PostgresqlTestForm()

    responsebody = current_user_repr()
    user_rep = responsebody['payload']

    if test_form.validate_on_submit():
        userdata_ = get_users_and_privs()
    
    print("!!!!!!!!")
    print(userdata_['payload'])
    print("!!!!!!!!!")
    return render_template(template_name_or_list='homepage.html', 
                           user=user_rep,
                           test_form=test_form,
                           userdata=userdata_['payload']
                           )