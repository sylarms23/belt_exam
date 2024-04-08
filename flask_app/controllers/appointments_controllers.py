#importaciones
from flask import Flask, render_template, request, redirect, session
from datetime import datetime, date

from flask_app import app

from flask_app.models.appointments import Appointment
from flask_app.models.usuarios import Usuario


#Rutas
@app.route('/new/appointment')
def new_appointment():
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/")
    
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)

    future_date = datetime.now().date()
    
    return render_template("new_appointment.html", usuario=usuario, future_date=future_date)


@app.route('/create/appointment', methods=["POST"])
def create_appointment():
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    if not Appointment.validate_appointment(request.form):
        return redirect("/new/appointment")
    
    Appointment.save(request.form)
    return redirect("/appointments")
    

@app.route('/edit/appointment/<int:id>')
def edit_appointment(id):
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)
    
    data_appointment  ={"id":id}
    appointment =Appointment.get_by_id(data_appointment)

    if appointment.usuario_id != session['usuario_id']:
        return redirect("/dashboard")

    return render_template('edit_appointment.html', appointment=appointment, usuario=usuario)


@app.route("/update/appointment", methods=["POST"])
def update_appointment():
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    if not Appointment.validate_appointment(request.form):
        return redirect("/edit/appointment/"+request.form['id'])
    
    Appointment.update_appointment(request.form)
    return redirect("/appointments")


@app.route("/delete/appointment/<int:id>")
def delete_appointment(id):
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    data_appointment  ={"id":id}
    Appointment.delete_appointment(data_appointment)

    return redirect("/appointments")







