
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.dojo_id = db_data['dojo_id']
        self.nombre = db_data['nombre']
        self.apellido = db_data['apellido']
        self.edad = db_data['edad']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['update_at']
        self.dojo = db_data['dojos.nombre']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        all_data = [] 

        for dojo in results:
            all_data.append( cls(dojo) )
        return all_data
    
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas JOIN dojos on  ninjas.dojo_id = dojos.id;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        print(results)

        all_data = [] 

        for dojo in results:
            all_data.append( cls(dojo) )
        return all_data

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM ninjas where id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)

        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO ninjas ( nombre, apellido, edad, dojo_id, created_at , update_at ) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(dojo_id)s,NOW(),NOW());"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET nombre=%(nombre)s,apellido=%(apellido)s, edad=%(edad)s, update_at=NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        return resultado