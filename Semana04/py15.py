#Aula 15

import csv
###########################################
#with open('names.csv', 'r') as csv_file:
#	csv_reader = csv.reader(csv_file)
#
#	next(csv_reader)
#
#	for line in csv_reader:
#		print(line[2])
#########################################
#with open('names.csv', 'r') as csv_file:
#	csv_reader = csv.reader(csv_file)
#
#	with open('new_names.csv', 'w') as new_file:
#		csv_reader = csv.reader(new_file,  delimiter='-')
#
#	for line in csv_reader:
#		csv_writer.writerow(line)
############################################################
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('new_names.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name', ' email']

		csv_writer = csv.DicWriter(new_fiel, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			csv_write.writerow(line)