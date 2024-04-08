#importaciones
from flask import Flask, render_template, request, redirect, session, flash
from datetime import datetime, date

from flask_app import app

from flask_app.models.usuarios import Usuario
from flask_app.models.appointments import Appointment

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#Rutas
@app.route('/')
def index():
    return render_template('login_registro.html')


@app.route("/registrar", methods=["POST"])
def registrar():

    if not Usuario.validar_usuario(request.form):
        return redirect("/")
    
    pass_encrypt = bcrypt.generate_password_hash(request.form["password"])
    form = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "correo": request.form['correo'],
        "password": pass_encrypt # AQUI SE GUARDA LA CONTRASEÑA ENCRIPTADA
    }

    nuevo_id = Usuario.guardar(form) #recibiendo el ID del nuevo Ususario
    session['usuario_id'] = nuevo_id
    return redirect("/appointments")
    
@app.route("/appointments")
def appointments():
    if 'usuario_id' not in session:
        return redirect("/")
    
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)

    appointments = Appointment.get_all()

    future_date = datetime.now().date()

    return render_template("appointments.html", usuario=usuario,appointments=appointments, future_date=future_date)


@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.obtener_por_correo(request.form) #usuario = instancia Usuario ó False

    print(usuario)

    if not usuario:
        flash("E-mail no registrado", "login")
        print("se deberia ejecutar el flash")
        return redirect("/")
    
    if not bcrypt.check_password_hash(usuario.password, request.form["password"]): #contraseña encriptada v/s contraseña no encriptada
        flash("Password incorrrecto", "login")
        return redirect("/")
    
    session['usuario_id'] = usuario.id #guardado en sesion el ID del usuario
    return redirect("/appointments")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")




