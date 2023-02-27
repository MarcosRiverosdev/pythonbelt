from Flask_app import app
from flask import render_template,redirect,request,session,flash
from Flask_app.models.user import User
from Flask_app.models.pie import Pie
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


@app.route('/')
def users():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['idsession'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def index():
    if 'idsession' not in session:
        return redirect('/logout')
    data ={
        'id': session['idsession']
    }
    return render_template("dashboard.html",user=User.get_id(data),pies=Pie.get_user_pies(data))

@app.route('/user/new', methods=['POST'])
def adduser():
    if not User.validate_register(request.form):
        return redirect('/')
    data={
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id =User.save_user(data)
    session['idsession']=id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')