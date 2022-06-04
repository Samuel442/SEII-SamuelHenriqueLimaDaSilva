#Aula 19

#li = [9,1,8,2,7,3,6,4,5]

#s_li = sortes(li, reverse=True)

#print('Sorted Variable:\t', s_li)

#li.sort(reverse=True)

#print('Original Variable:\t', s_li)

#li.sort(reverse=True)

#print('Original Variable:\t', li)
######################################
class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

# def e_sort(emp):
#	return emp.salary

s_employees = sorted(employees, key=lambda e: e.name)

print(s_employees)