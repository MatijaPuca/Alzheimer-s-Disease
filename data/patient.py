import mysql.connector
import datetime 
from .dbInfo import dbInfo
"""
    Responsible for 'Patient' database access
"""
class Patient:
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
        
        self.c = self.db.cursor(buffered=True)
    
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Adds a customer in database
        
        @param fields Data of the customer to be added
        @return Record of specified id
    """
    def add(self, fields):
        response = -1

        try:
            self.c.execute("INSERT INTO patient ( age, weight, height, patient_id, healthcare_id) VALUES (%s,%s,%s,%s,%s)", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            print(response)
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)
            

        
        return response

    def getId(self, username):
        response = -1
        
        try:
            self.c.execute("select user_id from user where username = %s",(username,) )
            self.db.commit()
            response = self.c.fetchone()
            print(response)
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response

    def getHealthcareProvider(self, healthcare_id):
        response = -1
        
        try:
            self.c.execute("select fname, lname from user where user_id = %s",(healthcare_id,) )
            self.db.commit()
            response = self.c.fetchone()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response
    """
        Returns all records in database
        
        @return List of all patients
    """
    def authenticate(self, fields):
        self.c.execute("SELECT * FROM user WHERE username=%s AND passw=%s", (fields[0], fields[1] ))
        results=self.c.fetchall()
        return results
    
    def getAll(self, id):
        self.c.execute("SELECT * FROM patient WHERE patient_id=%s", (id,))
        results=self.c.fetchall()
        #self.c.fetchall()
        return results
    
       
    def getAllHealthcareProviders(self):
        self.c.execute("SELECT username from user where isHealthcare = 1")
        results=self.c.fetchall()
        #self.c.fetchall()
        return results
    
    def close(self):
        self.db.close()
   
    
    """
        Returns the record with a specific id
        
        @param int id Id of the record
        @return Record of specified id
    """
    def get(self, id):
        self.c.execute("SELECT * FROM patient WHERE patient_id = %s", (id, ))
        return self.c.fetchone()
    
    """
        Updates a record in database
        
        @param fields Data of the customer to be updated
        @return List of affected database rows
    """
    def update_score(self, fields):
        self.c.execute("UPDATE patient SET score = %s WHERE user_id = %s",
        (
            fields[0],
            fields[1],
        ))
        self.db.commit()
        print(type(fields[1]))
        print(type(fields[0]))  

        return self.c.rowcount
    
    """
        Delete a patient in database
        
        @param Id of the patient
    """
    def delete(self, id_patient):
        self.c.execute("DELETE FROM patient WHERE id = %s", (id_patient, ))
        return self.c.rowcount
    


    """
        Updates the information column for patient
        
        @param fields Data of the customer to be updated ([info, id])
        @return List of affected database rows
    """
    def update_information(self, fields):
        self.c.execute("UPDATE patient SET Information = %s WHERE patient_id = %s",
        (
            fields[0],
            fields[1],
        ))
        self.db.commit()
        print(type(fields[1]))
        print(type(fields[0]))  
        return self.c.rowcount
    

    def setLifestyleData(self, fields):
        response = -1 
        try:
            self.c.execute("""UPDATE patient 
                              SET Information = %s
                              WHERE patient_id = %s;""", tuple(fields))
            self.db.commit()
            response = self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response