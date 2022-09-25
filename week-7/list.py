#x = ("theo","go", "koty")

#for i in x:
#    if i == "theo":
#        continue
#    else:
#        print(i)

#for e in range(1970,2023, 1):
#    print(e)

















#------------------------------------------------------------
x = 0
suum = 0
k = int(input())
k = k.lower() 
while k == True:
    if k != "q":
        return k
    elif k == "q":
        break
        print('You have decided to quit')
    suum = suum + k
    print(suum)
    x+=1


#x = list(range(10,1,-2))
#print(x)
#range function
#slogan = input()
#print("your slogan is empty") if slogan == "" else print(slogan.upper())




#............................................................................................
#raffle =[2,9,8]
#correct = []
#x = int(input(' enter first number: '))
#y = int(input(' enter second number: '))

#if x in raffle:
#    correct.append(x)
#if y in raffle:
#    if y != x:
#        correct.append(y)
#if len(correct) == 1:
#    print('You got ', len(correct), " number correctly")
#else:
#    print('You got ', len(correct), " numbers correctly")
#-------------------------------------------------------------------...............................

#if x in raffle and y in raffle:
#    print('you have entered two correct numbers')
#elif x in raffle or y in raffle:
#    print('you have entered one correct number')
#else:
#    print('you have entered two incorrect numbers')




# x = input('choose a user name:  ')

# if "admin" in x:
#    print('user name is not valid')
# else:
#    print('user name is valid') or pass










##assigning list to a tuple. we created a tuple x,y
# x = ['victor','sam']

# p,r = x
# print(p)








#x = (67,56,67,89)
#   updating the tuple

#x = (67,56,100) + x[3:]
#print(x)





#tuple can be converted to list and vice versa
#slice also works in tuple
#x = 13 , 12, 45
#x[1] = 100
#print(x)
# x = (6,8,89) this is a tuple
# y = 12,23,78 this is also a tuple
#print(x[0])
#y = tuple() creating a tuple

#maths =float(input('enter your maths score'))
#eng =float(input('enter your eng score'))
#science =float(input('enter your science score'))
#scores = [maths, eng, science]
#print(' your scores are ', scores)

#math = [23, 19, 25, 17,17,89,17, 23]
#eng = [23, 17, 20, 18]


#math.append(4)
#math.clear()
#math.append(60)
#math.extend(eng)
#print(math)
#x = math.count(25)
#print(x)
#x = math.index(17) tells the location of 17
#print(x)
#math.insert(0,60) 0 is the location, while 60 is the value to insert
#pop() removes the last item of a list
#math.reverse() reverses from front to back . same as [::-1]
#math.remove(23) removes the first 23. to remove the second, you type this again.
#math.sort() sorts from lowest to highest
#print(min(math)) prints the lowest value of math
#print(max(math))
#clear(math) clears everything inside math
#del(math) math deletes the whole of math
#print(min(math))

