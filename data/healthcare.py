import mysql.connector
import datetime 
from .dbInfo import dbInfo
class Healthcare:
    def __init__(self):
        self.db = mysql.connector.connect(
            database=dbInfo.db,
            host=dbInfo.server,
            user=dbInfo.user,
            password=dbInfo.password,
            charset="utf8"
        )


        self.c = self.db.cursor(buffered=True)

 
    def close(self):
        self.db.close()       


    def add(self, fields):
        response = 0
        try:
            self.c.execute("INSERT INTO healthcare (Score, healthcare_id) VALUES (%s,%s)", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)

    def getId(self, username):
        response = -1
        
        try:
            self.c.execute("select user_id from user where username = %s",(username,) )
            self.db.commit()
            response = self.c.fetchone()
            self.c.close()
            self.db.close()
            print("Successful")
            return response
        except Exception as e:
            print(e)              
        return response


    def getPatient(self, username):
        response = -1
        
        try:
            self.c.execute("""select u.*, c.* from user as u left join patient as c on u.user_id = c.patient_id
                                where username = %s""",(username,) )
            self.db.commit()
            response = self.c.fetchone()
            self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response


    def getPatientCount(self, id):
        response = -1
        
        try:
            self.c.execute("""select count(*) from patient where healthcare_id = %s""",(id,) )
            self.db.commit()
            response = self.c.fetchone()
            self.c.fetchall()

            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response



    def getPatients(self, id):
        response = -1
        
        try:
            self.c.execute("""select username from patient as c left join user as u 
                            on c.patient_id = u.user_id where c.healthcare_id = %s""",(id,) )
            self.db.commit()
            response = self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response


    def getGeneticsData(self):
        response = -1 
        try:
            self.c.execute("""select * from genetics_data""")
            self.db.commit()
            response = self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response

    def setGeneticsData(self, fields):
        response = -1 
        try:
            self.c.execute("""UPDATE patient 
                              SET geneticsData = %s
                              WHERE patient_id = %s;""", tuple(fields))
            self.db.commit()
            response = self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response
    
    def addPatientAssessment(self, fields):
        response = 0
        try:
            self.c.execute("""INSERT INTO mydb.food_logs(date, food_id, client_id, healthcare_id) VALUES (%s,%s,%s,%s)""", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)



    def getPatientCognitiveTest(self, fields):
        response = -1
        
        try:
            self.c.execute("""select exercise_name, category, calories from workout_logs natural join exercises as e
                                where client_id = %s and healthcare_id = %s 
                                and log_date = (select max(log_date) as dt from workout_logs 
                                where  client_id = %s and healthcare_id = %s)""",tuple(fields) )
            self.db.commit()
            response = self.c.fetchall()
            self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response
    