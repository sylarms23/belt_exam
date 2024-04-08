from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #es el encargado de mostrar errores
import re #importar las expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #expresion regular de correo


class Usuario:

    def __init__(self,data):
        #data(diccionario): {"id": 1, "nombre": "Elena", "apellido": "De troya",.....}
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls,form):
        #formulario = {"id": 1, "nombre": "Elena", "apellido": "De Troya","correo": "elena@codingdojo.com","password": YA ENCRIPTADA}
        query = "INSERT INTO usuarios (nombre, apellido, correo, password) VALUES (%(nombre)s,%(apellido)s, %(correo)s,%(password)s)"
        result = connectToMySQL('belt_exam').query_db(query,form) # Id del nuevo registro que se crea
        return result

    @staticmethod
    def validar_usuario(form):
        #form = {diccionario con todos los valores que el usuario ingreso}
        is_valid = True #asume que todos los valores cumplen con los requisitos

        #Validar que el nombre tenga al menos 2 caracteres
        if len(form["nombre"]) < 2:
            flash("Nombre debe tener al menos 2 cracteres", "register")
            is_valid = False

        #Validar que el nombre tenga al menos 2 caracteres
        if len(form["apellido"]) < 2:
            flash("Apellido debe tener al menos 2 cracteres", "register")
            is_valid=False
        
        #Que el correo tenga el patron correcto ---> Expresiones Regulares
        if not EMAIL_REGEX.match(form["correo"]):
            flash("E-mail invalido", "register")
            is_valid=False
        
        #validamos que el correo sea unico
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s"
        results = connectToMySQL('belt_exam').query_db(query,form)
        if len(results) >= 1:
            flash("E-mail registrado previamente", "register")
            is_valid=False
        
        #validar que la contraseña tenga al menos 6 caracteres
        if len(form["password"]) < 8:
            flash("Contraseña debe tener al menos 6 cracteres", "register")
            is_valid=False

        if form["password"] != form["confirm"]:
            flash("Contraseñas no coinciden", "register")
            is_valid=False

        return is_valid
    
    @classmethod
    def obtener_por_correo(cls,form):
        #form ={"correo": "elena@gd.com", "password": "Hola123"........}
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s "
        results = connectToMySQL('belt_exam').query_db(query,form)
        print(len(results))
        if len(results) == 1:
            # si existe el usuario, me regresa solo 1 reg. [0] /// si el usuario no existe la longitud es 0
            usuario = cls(results[0])
            return usuario #regreso la instancia del usuario con ese correo
        else:
            return False
        
    @classmethod
    def obtener_por_id(cls,form):
        #form {"id": 1}
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        results = connectToMySQL('belt_exam').query_db(query,form)#lista de diccionarios que en realidad es solo un diccionario con posicion 0
        usuario = cls(results[0])
        return usuario 

















    @classmethod
    def muestra_usuarios(cls):
        query ="SELECT * FROM usuarios"
        results = connectToMySQL('usuarios').query_db(query) # obtengo  una Lista de diccionarios
        """ 
        results = [
            {"id": 1, "nombre": "Elena", "apellido": "De Troya".......}
            {"id": 1, "nombre": "Juana", "apellido": "De Arco".......}
        ]
"""
        usuarios = []
        for us in results:
            #us  = {"id": 1, "nombre": "Elena", "apellido": "De Troya".......}
            usuario = cls(us) #instancia en base al diccionario que recibe
            usuarios.append(usuario) # se agrega cada instancia a la lista de usuarios[]
        return usuarios # Lista de objetos usuario
    
    
    
    @classmethod
    def borrar(cls, diccionario):
        query = "DELETE FROM usuarios WHERE id = %(id)s"
        result=connectToMySQL('usuarios').query_db(query, diccionario)
        return result
    
    @classmethod
    def mostrar(cls, diccionario):
        #diccionario = {"id": 1}
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('usuarios').query_db(query,diccionario) # Lista de diccionarios
        """ 
        result = [
            {"id": 1, "nombre": "Elena", "apellido": "De Troya".......} ----> 0
        ]
        """
        usuario = cls(result[0])
        return usuario

    @classmethod
    def actualizar(cls, formulario):
        #formulario = {"id": 1, "nombre": "Elena", "apellido": "De Troya",.............}
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido=%(apellido)s,correo=%(correo)s WHERE id=%(id)s"
        result = connectToMySQL('usuarios').query_db(query,formulario)
        return result

