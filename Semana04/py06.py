#Aula 06

language = 'Python'

if language == 'Python':
   print ('Language is Python')
else:
    print('No match')





language2 = 'Java'

if language2 == 'Python':
   print ('Language is Python')
elif language2 == 'Java':
    print ('Language is Java')
elif language2 == 'JavaSript':
    print ('Language is JavaScript')
else:
    print('No match')


#############################

user = 'Admin'
logged_in = False

if not logged_in:
    print ('Please Log In')
else:
    print: ('Welcome')

######################################


a =  [1,2,3]
b = a

print (id(a))
print (id(b))
print (id(a) == id(b))


######################################

condition = 'Test'

if condition:
   print ('Evaluated to True')
else:
    print ('Evaluated to False')