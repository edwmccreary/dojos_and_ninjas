from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.[class file name] import [class name]
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def read_all_dojos(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC"
        db_dojos = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []

        for dojo in db_dojos:
            dojos.append(cls(dojo))
        
        return dojos

    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)
    
    @classmethod
    def delete_dojo(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)

    @classmethod
    def read_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        read_dojo = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s"
        ninjas = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        dojo = cls(read_dojo[0])

        for ninja in ninjas:
            dojo.ninjas.append(Ninja(ninja))

        return dojo

#     @classmethod
#     def update_user(cls,data):
#         query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
#         return connectToMySQL("users_db").query_db(query,data)