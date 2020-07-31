from flask import Blueprint,render_template,request
from flask_login import current_user,login_user,logout_user
from .forms import LoginForm,RegistrationForm
from snap.models.users import User
from snap.utils.database import db


user_bp=Blueprint('users',__name__,template_folder='templates',static_folder='static')

@user_bp.route('/signup',methods=['GET','POST'])
def register():
    form=RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username=form.username.data
            email=form.email.data
            password=form.password.data

            new_user=User(username=username,email=email,password=password)

            db.session.add(new_user)
            db.session.commit()

            print("Added Success")



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