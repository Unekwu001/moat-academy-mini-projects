counter = 0
ticket_total = 0
while True:
    age = int(input('Please kindly enter your age:'))
    if age < 4:
        print('Your ticket is free')
    else:
        ticket_total = ticket_total + 100
        print('you have been charged 100 naira for the journey')
    if counter == 4:
        break
    counter+=1
print('The total charge for the 5 of you is: ',ticket_total)
print('Thanks for your patronage!')


