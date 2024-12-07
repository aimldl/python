# 1.Reading_CSV_files_in_Python-2.py
#
# https://pythonprogramming.net/reading-csv-files-python-3/
# Reading CSV files in Python
#
# reading_cvs_files_in_python-example.csv
# 1/2/2014,5,8,red
# 1/3/2014,5,2,green
# 1/4/2014,9,1,blue

import csv

with open('1.Reading_CSV_files_in_Python-example.csv') as file:
    csv_reader_inst = csv.reader(file,delimiter=',')
    dates = []
    colors = []
    for row in csv_reader_inst:
        color = row[3]
        date = row[0]
        
        dates.append( date )
        colors.append( color )
        
print( dates )
print( colors )

#  We are curious about what color something was on a specific date.
what_color = input('What color do you wish to know the date of?:')
color_index = colors.index(what_color)
the_date = dates[ color_index ]
print('The date of ', what_color, ' is ', the_date)
