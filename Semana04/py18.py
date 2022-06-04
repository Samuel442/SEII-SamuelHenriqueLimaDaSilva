#Aula 18

import builtins

#def min():
#	pass

#m = min([5, 1, 4, 2, 3])
#print(dir(builltins))

# x = 'global x'

#def test(z):
#	global x
#	x = 'local x'
#	print(y)
#	print(z)

#test('local z')
#print(z) 
###############################
def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()