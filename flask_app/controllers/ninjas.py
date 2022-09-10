from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/add_ninjas', methods=['POST', 'GET'])
def add_ninja():
    if  request.method == 'GET':
        dojos = Dojo.get_all()
        return render_template("add_ninjas.html", all_dojos = dojos)

    if  request.method == 'POST':
        Ninja.save(request.form)

        return redirect( '/')

@app.route('/ninjas')
def ver_ninjas():
    return render_template("ver_ninjas.html", ninjas=Ninja.get_all_ninjas())
