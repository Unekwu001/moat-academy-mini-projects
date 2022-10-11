#Try except is always good for file opening and importation errors and Rom space . for rom space you can use "except" only.
#except handles any other error while exception handles any other exception.
try:
    import home 
    height = float(input('enter your height: '))
    weight = input('enter your weight: ')
    bmi = float(weight)/(float(height)**2)
    print(f"your bmi is {bmi}")
    #b = lon
    #print(theo)
except ImportError:
    print('There is a problem with the import file')
except ZeroDivisionError:                               #trying to divide by zero
    print('You cannot divide by zero')
except NameError:                                       #unknown variable or undefined variable
    print(f'You have an undefined variable')
except ValueError:                                      #eg input letters for an int input
    print('cannot use letters')
except Exception:                                       #if something we cannot predict happens
    print('something happened')
else:
    print('good to go')
finally:                                  
    print('Have a nice day')                              

#we can also 
