from Flask_app import app
from flask import render_template,redirect,request,session,flash
from Flask_app.models.pie import Pie
from Flask_app.models.user import User


@app.route('/pie/new', methods=['POST'])
def addpie():
    if not Pie.validate_register(request.form):
        return redirect('/')
    data={
        "name": request.form['name'],
        "filling" : request.form['filling'],
        "crust" : request.form['crust'],
        "user_id" : session['idsession'],
    }
    id =Pie.save_pie(data)
    return redirect('/dashboard')

@app.route('/pie/<int:id>/edit')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_pie.html",pie=Pie.get_one_pie(data))

@app.route('/pies/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Pie.destroy(data)
    return redirect('/dashboard')

@app.route('/update/pie', methods=['POST'])
def updatepie():
    Pie.update_pie(request.form)
    return redirect('/dashboard')

@app.route('/pies')
def pies():
    return render_template("derby.html",pies=Pie.get_all_pies())

@app.route('/show/pie/<int:id>')
def showpies(id):
    data={
        'id':id
    }
    return render_template('show_pie.html',pies=Pie.get_one_pies_all(data))

@app.route('/pie/vote/<int:id>')
def vote(id):
    data={
        'id':id
    }
    Pie.vote(data)
    return redirect('/pies')