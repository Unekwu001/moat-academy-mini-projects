import csv

#with open('customers.csv','r') as file1:
#    myreader = csv.reader(file1) #there is also writer
#    for i in myreader:
#            print(i)


#myname = "theophilus shaibu"
#t = myname.replace(' ','_')
#print(t)













#k = open('v1.txt','r')
#c = k.read()


#s = open('empt.txt','w')
#s.write(c)


#s.close()
#k.close()


#with open('empty','a') as kojo:
#kojo.write()

























full_n = input("Enter your full name: ")
fullname = full_n.replace(' ','_')
Height = float(input("Enter your height in feets: "))
Weight = float(input("Enter your weight in kg: "))
BMI = Weight/(Height)**2

def bmi():
    if BMI < 18.5:
        return 'Remark: Underweight'
    elif BMI >= 18.5 and BMI <= 24.9:
        return 'Remark: Normal weight'
    elif BMI >= 25 and BMI <= 29.9:
        return 'Remark: Overweight'
    elif BMI >= 30:
        return 'Remark: Obesity'
    else:
        return 'Remark: Out of range'

with open(fullname+'_record.txt','w') as yea:
    yea.write(f'fullname: {full_n}\n Height: {Height}ft\n Weight: {Weight}kg \n {bmi()} ')

print(f'{fullname}_record.txt file created in this directory')





























#filename = input("supply file name")
#if filename.endswith(''):
#    print('pls supply a file extension with .txt')
#elif filename.endswith('.txt'):
#    with open(filename,'a') as fooo:
#        fooo.write('hallo')

        


























