
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:   
    def __init__( self , data ):
        self.id = data['id']
        self.nombre= data['nombre'] 
        self.created_at = data['created_at']
        self.update_at = data['update_at']

        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        all_data = []
        for dojo in results:
            all_data.append( cls(dojo) )
        return all_data



    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( nombre, created_at, update_at ) VALUES ( %(nombre)s, NOW() , NOW() );"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db( query, data ) 
        return  resultado  



    @classmethod
    def get_dojos_with_ninjas( cls, id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        data = {"id": id}
        print('ID', id)
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db( query, data)

        dojo = cls( results[0] ) if len(results) > 0 else  f'sin datos'   
        for row_from_db in results:                                                                         

            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "dojo_id" : row_from_db["dojo_id"],
                "nombre" : row_from_db["ninjas.nombre"],
                "apellido" : row_from_db["apellido"],
                'dojos.nombre' : row_from_db["nombre"],
                "edad" : row_from_db["edad"],
                "created_at" : row_from_db["ninjas.created_at"],
                "update_at" : row_from_db["ninjas.update_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo