#!/usr/bin/env python3
"""
test-list_of_lists2numpy_array_of_lists.py
The blog in Korea about this topic is at https://blog.naver.com/aimldl/221637320394

Google search: python list of lists to numpy array of lists
Referenced documents
(1) List of lists into numpy array, https://stackoverflow.com/questions/10346336/list-of-lists-into-numpy-array

There are at least 3 options:
1) Make an array of arrays:
  x=[[1,2],[1,2,3],[1]]
  y=numpy.array([numpy.array(xi) for xi in x])
  type(y)
  >>><type 'numpy.ndarray'> type(y[0]) >>><type 'numpy.ndarray'>
2) Make an array of lists:
  x=[[1,2],[1,2,3],[1]]
  y=numpy.array(x)
  type(y)
  >>><type 'numpy.ndarray'>
  type(y[0])
  >>><type 'list'>

3) First make the lists equal in length:
x=[[1,2],[1,2,3],[1]]
length = max(map(len, x))
y=numpy.array([xi+[None]*(length-len(xi)) for xi in x])
y
>>>array([[1, 2, None],
>>> [1, 2, 3],
>>> [1, None, None]], dtype=object)

(2) numpy.save(), https://www.geeksforgeeks.org/numpy-save/#targetText=numpy.save()%20function%20is,npy%20extension(.npy).&targetText=Parameters%3A,which%20the%20data%20is%20saved.&targetText=fix_imports%20%3A%20Only%20useful%20in%20forcing,a%20Python%202%20compatible%20way.
Code #1: Working
# Python program explaining  
# save() function   
import numpy as geek   
a = geek.arange(5)   
# a is printed. 
print("a is:") 
print(a)   
# the array is saved in the file geekfile.npy  
geek.save('geekfile', a)   
print("the array is saved in the file geekfile.npy") 
"""

import numpy as np

# input_list_of_lists
x = [['1'],
     ['1','2'],
     ['1','2','3'],
     ['1','2','3','4'],
     ['1','2','3','4','5']]

# Option 1: Make an array of arrays
y1 = np.array( [ np.array(xi) for xi in x] )
print( type( y1 ) )
'''
ipdb> y
array([array(['1'], dtype='<U1'), array(['1', '2'], dtype='<U1'),
       array(['1', '2', '3'], dtype='<U1'),
       array(['1', '2', '3', '4'], dtype='<U1'),
       array(['1', '2', '3', '4', '5'], dtype='<U1')], dtype=object)
'''

# Option 2: Make an array of lists
y2 = np.array( x )
print( type( y2 ) )
'''
ipdb> y2
array([list(['1']), list(['1', '2']), list(['1', '2', '3']),
       list(['1', '2', '3', '4']), list(['1', '2', '3', '4', '5'])],
       dtype=object)
'''

# option 3: First make the lists equal in length:
length = max( map(len, x) )
y3 = np.array( [xi+[None]*(length-len(xi)) for xi in x] )
print( type( y3 ) )
'''
ipdb> y3
array([['1', None, None, None, None],
       ['1', '2', None, None, None],
       ['1', '2', '3', None, None],
       ['1', '2', '3', '4', None],
       ['1', '2', '3', '4', '5']], dtype=object)
'''

# I choose option 2.
# Save y2 to file and load it to y2_loaded

# Save the array of lists to a .npy file
file = 'y2.npy'
np.save( file, y2 )

# Load the .npy file to variable y2_loaded
y2_loaded = np.load( file, allow_pickle=True )
print( type(y2_loaded) )
y2_loaded
'''
ipdb> y2_loaded
array([list(['1']), list(['1', '2']), list(['1', '2', '3']),
       list(['1', '2', '3', '4']), list(['1', '2', '3', '4', '5'])],
      dtype=object)
'''
