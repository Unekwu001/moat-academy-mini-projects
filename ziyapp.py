import mysql.connector
import re
import datetime

#when inside the class,refer to  admin as self.admin and others start with self.
class Ziya:
    """This models the functions with respect to what they have nd what they can do"""
     #class attributes are methods/functions and properties/variables
    admin =  "admin@ziya.com" # this is a class property
    

    def __init__(self): 
        self.company = "moat academy"
        #print(f'welcome to {self.company}')

    def upload_attachment(self):
        print(f"Attachment uploaded to {self.company} from {Ziya.admin}")
    
    def send_voice_message(self,attach=0):
        if attach == 1:
            self.upload_attachment()
            self.record_voice_message()
            print("message sent with attachment")
        elif attach == 0:
            self.record_voice_message()
            print('message sent')
        else:
            print('please kindly enter 0 or 1')

    def record_voice_message(self):
        print(f"voice message recorded in {self.company} ")



"""instantiation of ziya class """
if __name__ == "__main__":
    z = Ziya()
    z.send_voice_message(1)
#z.admin = "thhh"
#print(z.admin)
#print(Ziya.admin)
#z.upload_attachment()
    


#z.send_voice_message()
#print(z.__doc__)
#z = Ziya()
#z.admin ="hh"
#print(z.admin)
#print(Ziya.admin)
















