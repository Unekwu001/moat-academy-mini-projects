#import math 
#os module
#import os
#import sys

#At the last APC primaries, if the votes across the 6 geo political regions were recorded as follows:

votes = {
        "Bola Tinubu":[0, 200, 120, 0, 450, 670 ],
        "Yemi Osinbajo":[0,0, 0,56, 10,0],
        "Rochas Okorocha":[0,0,0,0,0,0],
        "Rotimi Amaechi":[20,13,2,1,29,0]
        }

g =[]
k = {i:sum(v) for i,v in votes.items()}
for y,p in k.items():
    g.append(p)
    if max(g) == p:
        print(f"{y} won the election with {p} votes")
    else:
        print(f'Sorry {y},You lost the election with {p} votes. try again in 2026')
k = ['theo', 8, 'kiop', 9]
print(*k, sep = ",")

#Write a program that goes through the dictionary/array and displays the name of the aspirant with the highest votes. Sample output would be: Bola Tinubu won the election with 1,440 votes







#k = {
#    "David":['Funke','Abim','Ben','Roman'],
#    "Leonard":['Olumide','Tade','Grace'],
#    "Kennedy":['Glory','Ada','Funke','Falz'],
#    "Neku":['Abim','Ben','Funke','Falz']
#    }


python = {2,3,4,5}
php = {4,60,3,10}
k = python.difference(php)
#i = python.union(php)
#u = print(i)
#counter = 1
#for i in range(6):



#-----------------------------------------------------------------------

#cohort22 = {
#            'php':['uche','zach','charles','leo','farouk'],
#            'python':['tolani','opeyemi','temy']
#            }

#php_students = []
#python_students = []

#for i,y in cohort22.items():
#    for c in y:
#        if i == 'php':
#            php_students.append(c)
#        elif i == 'python':
#            python_students.append(c)

#if len(php_students) > len(python_students):
#    print('Php students are more compared to python students')
#else:
#    printi('Python students are more')

#---------------------------------------------------------------------------






        
    



menu = ['Home', 'AboutUs', 'OurTeam']
#for i in menu:
#    if i == menu[-1]:
#        print(i)
#    else:
#        print(i, end=">>")
#print(*menu, sep =">>")
print(''.join(menu))





#counter = 1
#product = 1
#age = [23,31,38,19,26]
#for x in age:
#    product *= x
#print(product)


#for a,b in k.items():
#    print(b)









#def getName(a):
#    counter = 1
#    Cohort22 = ['David','Kennedy','Chinaza', 'Victoria', 'Olamide']
#    for i in Cohort22:
#        if i == a:
#            continue
#        else:
#            print(f"{counter}) {i}")
#            counter+=1
#getName('Kennedy')














#y = [x for a,b in k.items() for x in b if x == b[-1] ]







#for i in range(1,10,1):
#    for x in range(1,10,1):
#        print(i, 'x', x, '=', i*x)






















#b = os.getlogin()
#k = os.getcwd()
#c = os.listdir()



#markets = [['idumota','mile2','yaba'],
#            ['dugbe','bodija','sango'],
#            ['onitsha main','nnewi','post office']
#        ]
#students = [
#        ("Alejandro",["compsci","physics"]),
#        ("justin",["maths","compsci","stats"]),
#        ("ed",["compsci","accounting","economics"]),
#        ("maggot",["infsys","accounting","economics","commlaw"]),
#        ("peter",["sociology","economics","law","stats","music"])
#           ]



#k = "theophilus"
#y =  set(k)
#v = list(k)
#    print('True')
#else:
#    print('False')



#def jo(a):
#    for i in range(1,100,1):
#        if i == a:
#            continue
#        else:
#            print(i)
#k = jo
#k(5)
#------------------------------------------------------------------------------------------
# you can assign a function to a parameter
# a funcition can call another function
# a function can have a subfunction
# a function can take another function as argument
# functio can return another function
#def pure():
#    return 'my friend'


#def format_text(text):
#    print(f'you are welcome {text}')

#format_text(pure())






























#f = dict()
#for x,y in students:
#    f[x]= y
#print(f)

       
#f = { x:y for x,y in students if len(y) > 3}
#print(f)

#------------------------------------------------------------------------------------








#a = [[1,2,3],[10,20,30],[100,200,300]]

#b = []
#for i in aii:
#    for x in i:
#        b.append(x)
#print(b)

#b = [ x+10  for i in a for x in i  ]
#print(b)


#c = { x for}













#score = [67.3,78.1,89.5]
#for i in range(len(score)):
#    print(math.ceil(score[i]))  #rounds up to the closest higher whole number
#print(sys.path)


#username = "phpmyadmin"
#if username.endswith('admin'):
#    print('yes, it ends with admin')
#else:
#    print('no it doesnot end with admin')

#v =[]
#for i in os.listdir():
#    if i.endswith('.py'):
#        v.append(i)
#print(len(v))


#print(len(b))
#print(c)
#print(len(c))

#if len(c) < 10:
#    os.mkdir('extra')
#else:
#    print('folder is full')






#print(k)
#print(c)
#print(v)
