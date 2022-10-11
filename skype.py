from ziyapp import Ziya

#inheritance  1.upload_attachment can be overiden by defining upload_attachment() in class Skype.
#for multiple inheritance, when there is a name clash in the base classes, the first mentioned parent class will take priority

class InvalidCodeError(Exception):
    def __init__(self):
        self.message= "The code supplied is invalid"


class Skype(Ziya):

    def __int__(self):
        super().__init__()
        pass
    
    def upload_attachment(self):
        super().upload_attachment()
        print('hi')
    
    def send_voice_message(self,attach=0):
        if attach == 3:
            self.upload_attachment()
            self.upload_attachment()
        else:
            super().self.upload_attachment()

    def download_file(self,username):
        if username != "admin":
            try:
                raise InvalidCodeError
            except Exception as e:
                print(e.message)
        else:
            print('File downloaded successfully')

s = Skype()
#s.upload_attachment()
#s.send_voice_message(3)
s.download_file("admin")     










