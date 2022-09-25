product = 1
iteration_count = 0
total = 0
while True:
    x = input('Enter a number: ' )
    print('press q to quit')

    if x == "q" or x == "Q":
        break
    iteration_count +=1
    total = total + float(x)
    if x != 0:
        product = product * float(x)
print('The sum of all the numbers entered is:',total, ' The average is:',total/iteration_count, ' and The product is:',product)
print('Do have a nice day ahead!')






















#x = input()
#y = input()

#b = []
#b.append(int(x))
#b.append(int(y))
#print(b)
