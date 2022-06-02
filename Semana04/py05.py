#Aula 05

from multiprocessing.sharedctypes import Value


student = {'name': 'Jhon','age':25,'courses':['Math','CompSci']}
for key, value in student.items():
    print (key,value)