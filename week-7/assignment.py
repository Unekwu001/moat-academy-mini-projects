age = int(input('Enter your age: '))
y = input('Enter your party name: ')
party = y.lower()

if age < 70 and party == "apc":
    print('You are ineligible to contest because you are less than 70 years and from APC')
elif age < 70:
    print('You are ineligible to vote because you are less than 70 years of age')
elif party == "apc":
    print('You are ineligible to contest because you are less than 70 years and from APC')
elif age >= 70 and party != "apc":
    print('Congratulations!, you are eligible to contest.')
elif age >= 70 and party == "apc":
    print('You are ineligle to contest because you are a member of APC')
elif age <= 0:
    print('You havent been born yet, dont contest please!')
else:
    print('You have typed a wrong age')
        

