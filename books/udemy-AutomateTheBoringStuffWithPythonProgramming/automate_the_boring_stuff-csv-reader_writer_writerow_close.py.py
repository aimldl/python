#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
automate_the_boring_stuff-csv-reader_writer_writerow_close.py
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

### Reader Objects

"""

import csv

####################
#  Reader Objects  #
####################

exampleFile = open('example.csv')
exampleReader = csv.reader( exampleFile )
exampleData = list( exampleReader )
#[['2015-04-05 13:34', 'Apples', '73'],
# ['2015-04-05 3:41', 'Cherries', '85'],
# ['2015-04-06 12:46', 'Pears', '14'],
# ['2015-04-08 8:59', 'Oranges', '52'],
# ['2015-04-10 2:07', 'Apples', '152'],
# ['2015-04-10 18:10', 'Bananas', '23'],
# ['2015-04-10 2:40', 'Strawberries', '98']]

# exampleData[row][col] 
print( exampleData[0][0] )
# 2015-04-05 13:34

print( exampleData[6][1] )
# Strawberries

####################################################
#  Reading data from reader objects in a for loop  #
####################################################

for row in exampleData:
    print( row )
#    ['2015-04-05 13:34', 'Apples', '73']
#    Row #7 ['2015-04-05 13:34', 'Apples', '73']
#    ['2015-04-05 3:41', 'Cherries', '85']
#    Row #7 ['2015-04-05 3:41', 'Cherries', '85']
#    ['2015-04-06 12:46', 'Pears', '14']
#    Row #7 ['2015-04-06 12:46', 'Pears', '14']
#    ['2015-04-08 8:59', 'Oranges', '52']
#    Row #7 ['2015-04-08 8:59', 'Oranges', '52']
#    ['2015-04-10 2:07', 'Apples', '152']
#    Row #7 ['2015-04-10 2:07', 'Apples', '152']
#    ['2015-04-10 18:10', 'Bananas', '23']
#    Row #7 ['2015-04-10 18:10', 'Bananas', '23']
#    ['2015-04-10 2:40', 'Strawberries', '98']
#    Row #7 ['2015-04-10 2:40', 'Strawberries', '98']


#    print('Row #' + str( exampleReader.line_num) + ' ' + row)
#    TypeError: must be str, not list
    print('Row #' + str( exampleReader.line_num) + ' ' + str(row) )
    # Row #7 ['2015-04-05 13:34', 'Apples', '73']
    
    
####################
#  Writer Objects  #
####################
outputFile = open('output.csv','w',newline='')
outputWriter = csv.writer( outputFile )

# Writerow takes a list argument.
outputWriter.writerow( ['spam', 'eggs', 'bacon', 'ham'] )
outputWriter.writerow( ['Hello, world!','eggs','bacon','ham'] )
outputWriter.writerow( [1, 2, 3.141592, 4] )
outputFile.close()

#output.csv
#spam,eggs,bacon,ham
#"Hello, world!",eggs,bacon,ham
#1,2,3.141592,4

####################################
#  The delimiter & lineterminator  #
####################################

# .tsv (tab-seperated value)
csvFile = open( 'example.tsv', 'w', newline='' )
csvWriter = csv.writer( csvFile, delimiter='\t',lineterminator='\n\n')
csvWriter.writerow( ['apples','oranges', 'grapes'] )
csvWriter.writerow( ['eggs', 'bacon', 'ham'] )
csvWriter.writerow( ['spam', 'spam','spam','spam','spam','spam' ] )
csvFile.close()

#example.tsv
#apples	oranges	grapes
#
#eggs	bacon	ham
#
#spam	spam	spam	spam	spam	spam
