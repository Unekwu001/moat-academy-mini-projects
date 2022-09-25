usernames = []
passwords = []
login_details = []
#---------------------------------------------------------------------------------

def _signup(user,pwd):
    if user == "" or pwd == "":
        print("Username or passwords cannot be blank")
    elif user not in usernames:
        usernames.append(user)
        passwords.append(pwd)
        login_details.append({user:pwd})
        print('Sign up was successful')
    else:
        print('Username already exist')
    
#----------------------------------------------------------------------------------

def _login(user,pwd):
    login = {user:pwd}
    if login in login_details:
        print('You logged in successfully')
    else:
        print('your username or password is incorrect')

#-----------------------------------------------------------------------------------

def _reset_password(user,pwd,newpwd):
    login = {user:pwd}
    if login in login_details:
        login_details.remove(login)
        login = {user:newpwd}
        login_details.append(login)
        print('your password was changed successfully')
    else:
        print('your old password is incorrect')

#------------------------------------------------------------------------------------

if __name__ == "__main__":
    _signup('ola','1234')
    _signup('ade','4444')
    _login('ola','1234')
    _login('ola','12222')
    print(usernames)
    print(passwords)
    _reset_password('ola','355','567')
    _reset_password('ola','1234','343')
    print(login_details)









