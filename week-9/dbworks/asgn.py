import mysql.connector
from datetime import datetime,timedelta
#date_now = datetime.datetime.now()
#year = date_now.strftime('%Y')
#month = date_now.strftime('%B')
#week = date_now.strftime('%H')
#day = date_now.strftime('%M')
#print(date_now.strftime('%d,%a %b %Y'))



db = mysql.connector.connect(
host="localhost",
database="demoapp",
user="root",
password=""
        )

pen = db.cursor()

sql = "select * from customers"
pen.execute(sql)

records = pen.fetchall() #or fetchone or fetchmany
print("s/n,firstname, lastname,city,cust_regdate")
counter = 1
for i in records:
    h = i[6].strftime('%d, %a %b %Y')
    print(f"{counter}  {i[1]}   {i[2]}   {i[5]}   {h}")
    counter +=1
    






























#with open('suredotcom_staff.csv','r') as y:
#    v = csv.reader(y)    #there is also writer
#    v = list(v)

#val =[] 
#for c in v:
#    for t in c:
#        if t.endswith('@sure.com'):
#            val.append(tuple(c))

#sql = "insert into contact (id,name, email,message,regtime) values (%s,%s,%s,%s,%s)"

#pen.executemany(sql,val)
#mydb.commit()
#pen.close()
#mydb.close()














