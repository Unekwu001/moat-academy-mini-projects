import re
import datetime
import mysql.connector

class student:
    """This models the students with respect to what they have nd what they can do"""
    def showall(self):
        db = mysql.connector.connect(
                host = "localhost",
                database = "demoapp",
                user ="root",
                password = ""
                )
        pen = db.cursor()
        sql = "select * from contact"
        today = datetime.datetime.now()
        pen.execute(sql)
        y = pen.fetchall()
        print(y)



    def signup(self,message,email,fullname,pwd):
        db = mysql.connector.connect(
                host = "localhost",
                database = "demoapp",
                user ="root",
                password = ""
                )
        pen = db.cursor()
        pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])"
        today = datetime.datetime.now()
        sql = "insert into contact values(%s,%s,%s,%s,%s,%s)"
        val = (None,fullname,email,message,today,pwd)

        if re.match(pattern,pwd):
            pen.execute(sql,val)
            db.commit()
            fullname=fullname.replace(' ','_')
            with open(fullname+'.txt','w') as k:
                k.write(f"Welcome onboard to wedding app, your details are as follows:\n fullname:{fullname}\n email: {email}\n Thank you for joining")
        else:
            db.rollback()
            print("check your password")

        chk = pen.rowcount
        if chk > 0:
            print('signup successful')


    def login(self,username,password):
        print(f'login successful and your username is {username}')


    def check_result(self):
        print('you scored above average')


    def logout(self):
        pass

"""instatiation of a class below"""
x = student()
#x.signup('hello friend','hellorita@gmail.com','kenneth james','tuuudtytwWW42234')
x.showall()








