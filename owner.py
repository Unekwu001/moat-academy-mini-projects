class Owner:
    stock_items = ['biscuits','sweets','']
    def check_balance(self):
        print('the balance is 1200')

    def add_newstock(self):
        print('the item was added successfully')


    #@classmethod
    #def add_newstock(cls):
    #    print('the item added successfully')
#Owner.add_newstock()
    
    #@staticmethod #belongs to both the class and the object
    #def remove_stock():
    #    print('all stock items removed')
    #    cls.add_newstock()
#Owner.remove_stock() #or o.remove_stock()

o = Owner()
o.add_newstock()


