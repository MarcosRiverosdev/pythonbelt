from Flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Pie:
    def __init__(self,data) :
        self.id=data['id']
        self.name=data['name']
        self.first_name=data['filling']
        self.last_name=data['crust']
        self.password=data['user_id']
        self.vote=data['vote']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_user_pies(cls,data):
        query="SELECT * FROM pies where user_id=%(id)s"
        results=connectToMySQL('derbypie').query_db(query,data)
        pies=[]
        for valor in results:
            pies.append(cls(valor))
        return pies
    
    @classmethod
    def save_pie(cls,data):
        query="INSERT INTO pies (name,filling,crust,vote,user_id, created_at, updated_at) VALUES (%(name)s,%(filling)s,%(crust)s,0,%(user_id)s,now(),now());"
        result=connectToMySQL('derbypie').query_db(query,data)
        return result
    
    @staticmethod
    def validate_register(pie):
        is_valid=True
        if len(pie['name'])<1:
            flash('Name must be at  least 3 characters','register')
            is_valid=False
        if len(pie['filling'])<1:
            flash('Filling  must be at  least 3 characters','register')
            is_valid=False
        if len(pie['crust'])<1:
            flash('Crust  must be at  least 3 characters','register')
            is_valid=False
        return is_valid
    
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM pies WHERE id = %(id)s;"
        return connectToMySQL('derbypie').query_db(query,data)
    
    @classmethod
    def get_one_pie(cls,data):
        query  = "SELECT * FROM pies WHERE id = %(id)s;"
        result = connectToMySQL('derbypie').query_db(query,data)
        return result[0]
    
    @classmethod
    def update_pie(cls,data):
        query = "UPDATE pies SET name=%(name)s,filling=%(filling)s,crust=%(crust)s,updated_at=NOW() WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('derbypie').query_db(query,data)
    
    @classmethod
    def get_all_pies(cls):
        query="select * from pies inner join USER ON pies.user_id=user.id"
        results=connectToMySQL('derbypie').query_db(query)
        pies=[]
        for valor in results:
            pies.append(cls(valor))
        return pies

    @classmethod
    def get_one_pies_all(cls,data):
        query="select * from pies inner join USER ON pies.user_id=user.id where pies.id=%(id)s"
        results=connectToMySQL('derbypie').query_db(query,data)
        return results[0]
    
    @classmethod
    def vote(cls,data):
        query="UPDATE pies set vote=vote+1 where id=%(id)s"
        return connectToMySQL('derbypie').query_db(query,data)
        