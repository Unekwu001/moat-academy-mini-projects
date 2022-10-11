import re

ph =['0803472894','aertyujhgf','123456','0706234567','080912345i6','nrtetii0987','00965498765','08075643232','_)(&%^']
#g =[]
#for i in ph:
#    if len(i) == 11 and (i.startswith('080') or i.startswith('090') or i.startswith('070') or i.startswith('081')) and i.isdigit():
#        g.append(i)
#print(g)

#  re.findall()  #returns a list of matches
#  re.match()    #obj/none returns  if found aat the beginning
#  re.search()   #obj/none
#sub()
#split()
#\A for beginning
#\b for begininng and end
#\B for within but not at the end and beginning
#\d if it is digit
#\D if string does not contain digit
#nal$ ends with 'nal'

#for i in ph:
#    if re.search(r'\D',i) == False and len(i) == 11:
#        print(i)
#k = "^080"
#patern = "^(080) [\d] {8}$" #this means starts with 080 continues and ends with 8 digits.
#userinput = 'tghfgjidgaehjhakhgff'
#d = (aa)* # when 'aa' occur zero or more times
#dd = (aa)+ #when 'aa' occurs 1 or more times

#print(re.findall('[a-e]',userinput))
#x = re.match(pattern,userinput)
# print(x.group())
#
pattern = "^([a-z]+)([a-z|0-9]+)@[a-z]{5}[.][a-z]+$"
c =["tusedor360@gmail.com","theophilusshaibu@gmail.com","unekwutheophilus","youtuba@gmail"]
for i in c:
    if re.search(pattern,i):
        print('nice')
    else:
        print('naaaaaaaaaa')


#userinput = """there aire many 7574 9034 words here that are 234, 678 anf 69798"""
#print(re.split(" ",userinput))
#strr = "xyz@gmail.com"


#email = "tolanigiwa360@gmail.com"
#pat = "^(\D){10}[\d]{3}[a][gmail][.][com]"
#y = re.search(pat,email)
#print(y)






#x = re.sub(patern3,'_',)
#print(y)














































