from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import current_user,login_user,logout_user
from .forms import LoginForm,RegistrationForm
from snap.models.users import User
from snap.utils.database import db


user_bp=Blueprint('users',__name__,template_folder='templates',static_folder='static')

@user_bp.route('/home')
def home():
    return render_template('users/home.html')

@user_bp.route('/signup',methods=['GET','POST'])
def register():
    form=RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username=form.username.data
            email=form.email.data
            password=form.password.data

            new_user=User(username=username,email=email)

            new_user.generate_password(password)

            new_user.create()

            flash("User created Successfully")


            return redirect(url_for('users.login'))

    context={
        'form':form
    }
    return render_template('users/register.html',**context)

@user_bp.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()


    username=form.username.data
    password=form.password.data


    user=User.query.filter_by(username=username).first()




    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for('users.home'))

    

    context={
        'form':form
    }
    return render_template('users/login.html',**context)

@user_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))