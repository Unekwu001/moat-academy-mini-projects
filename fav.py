allowed =['lai','ffk','omale']
def deco(fn):
    def wrapper():
        x = input('Enter your name: ')
        x = x.lower()
        if x in allowed:
            fn()
        else:
            print('results are being collated')
    return wrapper

@deco
def show_result():
    print("soludo won the election")


def ceremony():
    print("the swearing in of the ceremony for soludo is on march 23")

show_result()

#y = deco(ceremony)
#y()













def senior_deco(i):
    def deco(fn):
        """This is a decorator"""
        def wrapper(c):
            print(i*20)
            fn(c)
            print(i*20)
        return wrapper
    return deco


@senior_deco('*')                                                               #deco does the job but senior determines what deco uses
def greetings(username):
    print(f'Hello {username}, what do you want to do today')

greetings('Funmi')












