from flask_login import logout_user, login_required
from flask import Blueprint, render_template, redirect, url_for

from ..forms import LoginForm
from ..services.user_service import login


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login_():
    form = LoginForm()
    if form.validate_on_submit(): 
        responsebody = login(username=form.username.data, password=form.password.data)
        if responsebody['message']['category'] == 'success':
            return redirect(url_for('home.homepage'))
    return render_template('login.html', form=form)



@auth.route('/logout')
@login_required
def logout_():
    logout_user()
    return redirect(url_for('home.homepage'))