import mysql.connector
import datetime 
from .dbInfo import dbInfo

"""
    Responsible for 'Users' database access
"""
class User:
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.db = mysql.connector.connect(
            database=dbInfo.db,
            host=dbInfo.server,
            user=dbInfo.user,
            password=dbInfo.password,
            charset="utf8"
        )
        
        self.c = self.db.cursor()
    
    def close(self):
        self.db.close()
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------


    def add(self, fields):
        response = 0
        
        try:
            self.c.execute("INSERT INTO user (email, username, passw, fname, lname, isHealthcare) VALUES (%s,%s,%s,%s,%s,%s)", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            self.c.close()
            self.db.close()
            print("Added to the database")
            return response
        except Exception as e:
            print(e)
            


    def authenticate(self, fields):
        response = 0

        try:
            self.c.execute("SELECT * FROM user WHERE username=%s AND passw=%s", tuple(fields))
            response=self.c.fetchone()
            print(response)
            return response
        
        except Exception as e:
            print(e)