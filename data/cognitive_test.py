import mysql.connector
import datetime 
from .dbInfo import dbInfo

"""
    Responsible for 'Cognitive_Tests' database access
"""
class Cognitive_Tests:
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
            self.c.execute("INSERT INTO cognitive_tests (patient_id, test_answer, date_taken) VALUES (%s,%s,%s)", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            self.c.close()
            self.db.close()
            print("Added to the database")
            return response
        except Exception as e:
            print(e)