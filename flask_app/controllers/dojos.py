from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


#aca en el controlador se ingresan las rutas
@app.route('/', methods=['POST', 'GET'])
def add_dojos():
    if  request.method == 'GET':
        dojos = Dojo.get_all()
        return render_template("add_dojos.html", all_dojos = dojos )
    
    if  request.method == 'POST':
        
        data = {
            'nombre': request.form['nombre']
        }

        Dojo.save(data)
        return redirect( '/')

@app.route('/dojos/<int:id>')
def show_dojos(id):
    dojo = Dojo.get_dojos_with_ninjas(id)
    
    return render_template("show_dojo.html", dojo = dojo)

