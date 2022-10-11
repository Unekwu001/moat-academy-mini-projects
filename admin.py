import mysql.connector
from latecomer import Participants

class Admin(Participants):
    """This class handles all admin functionalities"""
    def __init__(self):
        self.db = mysql.connector.connect(
                    host = "localhost",
                    database = "demoapp",
                    user ="root",
                    password = ""
                    )
        self.pen = self.db.cursor()

    def login(self,name,pwd):
        sql = "select * from admin_user where admin_username=%s and admin_pwd=%s"
        val = (name,pwd)
        self.pen.execute(sql,val)
        k = self.pen.fetchone()
        if k:
            print('you have logged in')
        else:
            print('invalid credentials')

    def ban_user(self,username):
        name=input('enter a name')
        pwd = input('enter a password')
        self.login(name,pwd)
        sql = "update participant set status=%s where email=%s"
        val = ('inactive',username)
        self.pen.execute(sql,val)
        self.db.commit()
        if self.pen.rowcount:
            print('you have been banned')
        else:
            print('please try again')




a = Admin()
#a.login('theo','6775')
a.ban_user('tusedortolasha@gmail.com')
a.register()



