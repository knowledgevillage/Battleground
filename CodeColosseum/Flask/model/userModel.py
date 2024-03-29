import mysql.connector
import json
from flask import make_response


class userModel():

 # defining a constructor to initialize objects/ connetion at the invocation of this call itself
    def __init__(self): 
         #connection Establishment code
        try:
            self.con=mysql.connector.connect(host="localhost", user="root", password="B@ttlef!ld$123", database="flaskbattlefield")
            print("connection successful")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)

        except:
            print("some Error")
        

# Method to get all details
    def userGetAllModel(self):
        self.cur.execute("select * from usercontrol")
        result=self.cur.fetchall()
        print(result)
        if len(result)>0:
            res=make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return make_response({"message":"No Data Found"},204)

# Method to insert a record in the database  
    def userAddOneModel(self, data):
        self.cur.execute(f"insert into usercontrol(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        #print(data)
        return make_response({"message":"User created successfully"},201)


# Method to update the record in database
    def userUpdateModel(self, data):
        self.cur.execute(f"update usercontrol set name='{data['name']}', email='{data['email']}' , phone='{data['phone']}' , role='{data['role']}' , password='{data['password']}' where id={data['id']} ")
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfully"},201)
        else:
            return make_response({"message":"No thing to update"},202)


# Method to delete record in database
    def userDeleteModel(self, data):
        self.cur.execute(f"Delete from usercontrol where id ={data} ")
        if self.cur.rowcount>0:
            return make_response({"message":"User Deleted successfully"},201)
        else:
            return make_response({"message":"No thing to delete"},202)
        

# Method to update a record with dynamic information
    def userPatchModel (self,data, id):
        qry="update usercontrol set "
        for key in data:
            qry+= f"{key}='{data[key]}',"
        qry=qry[:-1]
        qry+=f" where id={id}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfully"},201)
        else:
            return make_response({"message":"No thing to update"},202)



# Method to get all details in pagintation fasion
    def userPaginationModel(self, limit, page):
        limit=int(limit)
        page=int(page)
        start = (page*limit) - limit
        print(f"start is {start}")
        qry=f"select * from usercontrol limit {start} , {limit}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        print(result)
        if len(result)>0:
            res=make_response({"payload":result, "page_no":page , "limit": limit},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return make_response({"message":"No Data Found"},204)
        

            

# Method to update the record in database
    def userUploadAvtarModel(self, uid, finalFilePath):
        self.cur.execute(f"update usercontrol set avtar ='{finalFilePath}' where id= {uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"User uploaded successfully"},201)
        else:
            return make_response({"message":"No thing to update"},202)
