#Aula 20

try: 
	f = open('test_file.txt')
	var = bad_var
	
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
finally:
	print("Executing Finally...")