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


    def requestAccept(self, fields):
        response = 0
        try:
            self.c.execute("""UPDATE client SET healthcare_id = %s WHERE client_id = %s""", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)


    def clearRequest(self, fields):
        response = 0
        try:
            self.c.execute("""delete from requests where healthcare_id = %s and client_id = %s""", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)




    def getRequests(self, id):
        response = -1
        
        try:
            self.c.execute("""select username from requests as r left join user as u 
                            on r.client_id = u.user_id where healthcare_id = %s""",(id,) )
            self.db.commit()
            response = self.c.fetchall()
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
            self.c.close()
            self.db.close()
            print("Successful")
            return response
        except Exception as e:
            print(e)              
        return response


    def getClient(self, username):
        response = -1
        
        try:
            self.c.execute("""select u.*, c.* from user as u left join client as c on u.user_id = c.client_id
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


    def getClientCount(self, id):
        response = -1
        
        try:
            self.c.execute("""select count(*) from client where healthcare_id = %s""",(id,) )
            self.db.commit()
            response = self.c.fetchone()
            self.c.fetchall()

            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response



    def getClients(self, id):
        response = -1
        
        try:
            self.c.execute("""select username from client as c left join user as u 
                            on c.client_id = u.user_id where c.healthcare_id = %s""",(id,) )
            self.db.commit()
            response = self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response


    def getWorkouts(self):
        response = -1
        
        try:
            self.c.execute("""select * from exercises""")
            self.db.commit()
            response = self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response


    def getFoods(self):
        response = -1
        
        try:
            self.c.execute("""select * from foods""")
            self.db.commit()
            response = self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response


    def addWorkout(self, fields):
        response = 0
        try:
            self.c.execute("""INSERT INTO mydb.workout_logs(log_date, exercise_id, client_id, healthcare_id) VALUES (%s,%s,%s,%s)""", tuple(fields))
            self.db.commit()
            response = self.c.rowcount
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)


    def addFood(self, fields):
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



    def getClientWorkouts(self, fields):
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
    

    def clearClientWorkouts(self, fields):
        response = -1
        
        try:
            self.c.execute("""delete from workout_logs 
                        where client_id = %s and healthcare_id = %s
                        and log_date = %s""",tuple(fields) )
            self.db.commit()
            response = self.c.fetchall()
            self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response

    def clearClientNutrition(self, fields):
        response = -1
        
        try:
            self.c.execute("""delete from food_logs 
                        where client_id = %s and healthcare_id = %s
                        and date = %s""",tuple(fields) )
            self.db.commit()
            response = self.c.fetchall()
            self.c.fetchall()
            self.c.close()
            self.db.close()
            return response
        except Exception as e:
            print(e)              
        return response


    def getClientNutrition(self, fields):
        response = -1
        
        try:
            self.c.execute("""select food_name, diet, calories from food_logs natural join foods as e
                                where client_id = %s and healthcare_id = %s 
                                and date = (select max(date) as dt from food_logs 
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