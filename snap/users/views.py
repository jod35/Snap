from flask import Blueprint,render_template
from flask_login import current_user,login_user,logout_user
from .forms import LoginForm,RegistrationForm


user_bp=Blueprint('users',__name__,template_folder='templates',static_folder='static')

@user_bp.route('/signup',methods=['GET','POST'])
def register():
    form=RegistrationForm()

    context={
        'form':form
    }
    return render_template('users/register.html',**context)

@user_bp.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()

    context={
        'form':form
    }
    return render_template('users/login.html',**context)