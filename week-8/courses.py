
from payment import pay_tuition as p
#import onboarding as o
#from onboarding import login                    #cool
from onboarding import signup as sp             #used to prevent clashes


def register():
    p()
    print('you are here to register')

def check_lecturer():
    print('herev are your lecturers')



register()
sp('theophilus', '4535')
#print(usernames)
#print(onboarding.passwords)
#onbording.login('theophilus','45356')
