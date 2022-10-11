import mysql.connector

#print("welcome {}".format(l))
#hon = "rohh"
#l ="John"
#print("welcome %s" %l)
#j = 50.6
#k = 80.5
#print("j  is equal to  %f and k is equal to %f  and my name is %s and my favorite letter is %s" %(j,k,l, hon))
try:
    mydb = mysql.connector.connect(
        host="localhost",
        database="demoapp",
        user="root",
        password=""
        )

    cursor_obj = mydb.cursor()
    

    name=input('enter your name: ')
    email= input('enter your email: ')
    message =input('enter a message: ')
    name1=input('enter your name11: ')
    email1= input('enter your email11: ')
    message1 =input('enter a message11: ')


    #cursor_obj.execute("insert into  contact SET name=' %s ', email=' %s ', message=' %s ' " %(name,email,message))
    #cursor_obj.execute(f"insert into  contact values('0','{name}','{email}','{message}')")
    
    #or below due to sql injection(hackers) This recommended----------------------------

    sql = "insert into contact (name, email,message) values (%s,%s,%s)"
    #val = (name,email,message)
    
    val = [(name,email,message),(name1,email1,message1)]
    #cursor_obj.execute(sql,val)

    cursor_obj.executemany(sql,val)
    #cursor_obj.execute("delete from contact  where id = 8 ; ")
    #chek = cursor_obj.lastrowid
    chek = cursor_obj.rowcount

    if chek:
        print('your record has been inserted')
    else:
        print('please try again')
#mydb.is_connected()
#print(mydb.get_server_info())
except mysql.connector.Error as e:
    print('Database error!', e)
    mydb.rollback()
except Exception as c:
    print(c)
else:
    print('successful')
    mydb.commit()
    cursor_obj.close()
    mydb.close()




















