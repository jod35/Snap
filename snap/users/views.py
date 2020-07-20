from flask import Blueprint

user_bp=Blueprint('user_bp',__name__,template_folder='templates')


@user_bp.route('/login')
def login():
    return 'Login Page'