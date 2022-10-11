import mysql.connector

class Participants:

    def __init__(self,option):
        self.option = option
        self.username = ""
        self.password = ""
        self.db = mysql.connector.connect(
                host = "localhost",
                database = "demoapp",
                user ="root",
                password = ""
                )
        self.pen = self.db.cursor()


    def login(self,user_name,user_password):

        sql = "select * from participant where fullname =%s and pwd=%s and status=%s"
        val = (user_name,user_password,"active")
        self.pen.execute(sql,val)
        self.pen.fetchone()
        if self.pen.fetchone():
            print("log in successful")
        else:
            print("something went wrong, check your password or username")



    def register(self,name,mail,password):
        sql = "insert into participant(Fullname,email,pwd) values(%s,%s,%s)"
        val = name,mail,password

        self.option = self.option.upper()
        if self.option == "PHP" or self.option == "PYTHON":
            self.pen.execute(sql,val)
            self.db.commit()    
            print(f'congrats {name}, you have registered for {self.option} class')
        else:
            print(f"{self.option} is not valid, please input 'php' or 'python' or account disabled")

        chk = self.pen.rowcount
        if chk > 0:
            self.username = name
            self.password = password
            print(f'{chk} record inserted successfully')
        else:
            print('insert was not successful')

p = Participants("python")
p.register('bilyl grate','tusredorrtolasha@gmail.com','tu34ss32dsde808')
#p.login('bill gate','tu3432dsde808')
#p.login()
#print(p.username)





