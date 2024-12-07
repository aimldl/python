#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
automate_the_boring_stuff-csv-remove_csv_header.py

Removes the header from all CSV files in the current working directory.


Ch14_Working_with_CSV_Files_and_JSON_Data

# Automate the Boring Stuff with Python
https://automatetheboringstuff.com/

## Chapter 14 – Working with CSV Files and JSON Data
https://automatetheboringstuff.com/chapter14/

### Summary
CSV and JSON are common plaintext formats for storing data.
They are easy for programs to parse while still being human readable,
so they are often used for simple spreadsheets or web app data.

The csv and json modules greatly simplify the process of 
  reading and writing to CSV and JSON files.
  
Reading CSV files in Python
https://pythonprogramming.net/reading-csv-files-python-3/

14.1. csv — CSV File Reading and Writing
https://docs.python.org/3/library/csv.html

Skip the header of a file with Python's CSV reader
https://evanhahn.com/python-skip-header-csv-reader/

with open('mycsv.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
    next(csvreader)

    for row in csvreader:
        # do stuff with rows..
  
"""
#################################################
#  Project: Removing the Header from CSV Files  #
#################################################

import os
import csv

# Step 1: Loop Through Each CSV File
os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # Skip non-csv files
    
    print('Removing header from '+ csvFilename + '...')
    
    # Step 2: Read in the CSV File
    # Open the file object
    with open( csvFilename ) as csv_file_obj:
        # Read in the csv file
        csv_reader_obj = csv.reader( csv_file_obj)

#       The following lines work, too. But I'll use next(...).
#        new_row = []
#        for row in csv_reader_obj:
#            if csv_reader_obj.line_num == 1:
#                continue  # Skip the first row
#            new_row.append( row )
        
        # Skip the first row.
        next( csv_reader_obj )
        # From the second row, save the row to new_row
        new_row = []
        for row in csv_reader_obj:
            new_row.append( row )
            #print( row )
    
    # Step 3: Write Out the CSV File Without the First Row
    # Write out the csv file.
    # TODO: Generalize this part
    output_file = 'output_without_header.csv'
    with open( output_file, 'w') as ouput_file_obj:
        csv_writer_obj = csv.writer( ouput_file_obj )
        
        for row in new_row:
            csv_writer_obj.writerow( row )
