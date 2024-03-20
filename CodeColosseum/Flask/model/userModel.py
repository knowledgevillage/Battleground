import mysql.connector
import json
from flask import make_response
class userModel():
    def __init__(self): # it's a contructor 
         #connection Establishment code
        try:
            self.con=mysql.connector.connect(host="localhost", user="root", password="B@ttlef!ld$123", database="flaskbattlefield")
            print("connection successful")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)

        except:
            print("some Error")
        

    def userGetAllModel(self):
        self.cur.execute("select name, email, phone, role, password from usercontrol")
        result=self.cur.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No Data Found"},204)
        
    
    
    def userAddOneModel(self, data):
        self.cur.execute(f"insert into usercontrol(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        #print(data)
        return make_response({"message":"User created successfully"},201)
    

    def userUpdateModel(self, data):
        self.cur.execute(f"update usercontrol set name='{data['name']}', email='{data['email']}' , phone='{data['phone']}' , role='{data['role']}' , password='{data['password']}' where id={data['id']} ")
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfully"},201)
        else:
            return make_response({"message":"No thing to update"},202)
            
    def userDeleteModel(self, data):
        self.cur.execute(f"Delete from usercontrol where id ={data} ")
        if self.cur.rowcount>0:
            return make_response({"message":"User Deleted successfully"},201)
        else:
            return make_response({"message":"No thing to delete"},202)
