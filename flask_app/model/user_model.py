import mysql.connector as sql
import re

class userModel():
    def __init__(self):
        # write connection for mysql db
        try:
            self.con = sql.connect(
                host = "localhost",
                user = "root",
                password = "pranali",
                database = "api_tables"
            )
            self.cursor = self.con.cursor(dictionary=True)
            self.con.autocommit = True
            print("connection successful..!")
            
            

        except:
            print("connection error!")
            
            
    def user_getall_model(self):
        try:

            result = self.cursor.execute("SELECT * FROM api_tables.user")
            result = self.cursor.fetchall()

            return result
    
        except:
             print("connection error!")

    def user_add_model(self,data):
        # sql syntax for insert user data
        self.cursor.execute((f"INSERT INTO user (FirstName, LastName, ContactNumber, email, password) VALUES('{data['FirstName']}', '{data['LastName']}', '{data['ContactNumber']}', '{data['email']}', '{data['password']}')"))
        return "User data added successfully...!"      

    def user_insert_model(self,data):
        # sql syntax for insert user data
        msg='[]'
        regex=r'\b[A-Za-z0-9._%+-]+@[gmail]+\.[com]{2,7}\b'
        #regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email= data['email']
        print(email)
        def check():
            if (re.match(regex, email)):
           
                self.cursor.execute((f"INSERT INTO user (FirstName, LastName, ContactNumber, email, password) VALUES('{data['FirstName']}', '{data['LastName']}', '{data['ContactNumber']}', '{data['email']}', '{data['password']}')"))
                msg= "User data added successfully...!"  
                return msg
            else:
                msg= "Please insert valid gmail id...!"  
                return msg  
        #check()
        return check()