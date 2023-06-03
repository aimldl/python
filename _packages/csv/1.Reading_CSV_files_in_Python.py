# 1.Reading_CSV_files_in_Python.py
#
# https://pythonprogramming.net/reading-csv-files-python-3/
# Reading CSV files in Python

# reading_cvs_files_in_python-example.csv
# 1/2/2014,5,8,red
# 1/3/2014,5,2,green
# 1/4/2014,9,1,blue

import csv

with open('1.Reading_CSV_files_in_Python-example.csv') as csvfile:
	csv_reader_inst = csv.reader(csvfile, delimiter=',')
	for row in csv_reader_inst:
		print(row)
		print(row[0])
		print(row[0],row[1],row[2])
