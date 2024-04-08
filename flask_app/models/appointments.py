from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 


class Appointment:

    def __init__(self,data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']

        self.nombre_usuario = data["nombre_usuario"]


    @classmethod
    def save(cls,form):
        query = "INSERT INTO appointments (task, date, status, usuario_id) VALUES (%(task)s,%(date)s, %(status)s,%(usuario_id)s)"
        result = connectToMySQL('belt_exam').query_db(query,form) # Id del nuevo registro que se crea
        return result

    @staticmethod
    def validate_appointment(form):
        is_valid = True #asume que todos los valores cumplen con los requisitos

        if len(form["task"]) < 2:
            flash("Task debe tener al menos 2 cracteres", "validate_appointment")
            is_valid = False

        if form['date'] == "":
            is_valid = False
            flash("Ingresa una fecha de creacion", "validate_appointment")

        if form['status'] == "":
            is_valid = False
            flash("Selecciona un estado", "validate_appointment")

        return is_valid
    
    @classmethod 
    def get_all(cls):
        query = "SELECT appointments.* , usuarios.nombre as nombre_usuario FROM appointments JOIN usuarios ON appointments.usuario_id = usuarios.id"
        results = connectToMySQL('belt_exam').query_db(query) #Lista de diccionarios
        appointments =[] 
        for appointment in results:
            appointments.append(cls(appointment)) 
        return appointments
        
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT appointments.* , usuarios.nombre as nombre_usuario FROM appointments JOIN usuarios ON appointments.usuario_id = usuarios.id WHERE appointments.id = %(id)s"
        results = connectToMySQL('belt_exam').query_db(query,data)
        appointment = cls(results[0])
        return appointment 
    

    @classmethod
    def update_appointment(cls, form):
        query = "UPDATE appointments SET task = %(task)s, date = %(date)s, status = %(status)s WHERE id  = %(id)s"
        result  =connectToMySQL('belt_exam').query_db(query, form)
        return result

    
    @classmethod
    def delete_appointment(cls, data):
        query = "DELETE FROM appointments WHERE id = %(id)s"
        result=connectToMySQL('belt_exam').query_db(query, data)
        return result
    



