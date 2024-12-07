# udacity-ds_and_algos-lesson2-python_refresher-function_and_generator-exercise2.py

#Define a procedure, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and
# returns the boolean True if the input is a valid sudoku square and 
# returns the boolean False otherwise.
#
#A valid sudoku square satisfies these two properties:
#   1. Each column of the square contains each of the whole numbers from 1 to n exactly once.
#   2. Each row of the square contains each of the whole numbers from 1 to n exactly once.

# solution.py

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_sudoku(square):
    for row in square:
        check_list = list( range(1, len(square[0])+1) )
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
        
    for n in range( len(square[0]) ):
        check_list = list( range(1, len(square[0])+1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove( row[n] )
    return True

# my_solution.py
# TODO:
#   Fix from incorrect4
#   I need to check if the value v is integer and return False if not.
#   The following lines are errorneous.
#          if v.isdecimal() == False:
#              return False
#    if v.isdecimal() == False:
#   AttributeError: 'int' object has no attribute 'isdecimal'

#def check_sudoku( square):
#    l = len(square)
#    #print(l)
#    flag = []
#    # Check the rows
#    for r in range(l):
#        # Initialize flag to zero
#        for c in range(l):
#          flag.append( 0 )
#          #print(flag)
#          #print( c, flag[c] )
#          
#        #  Use flag
#        for c in range(l):
#          v = square[r][c]
#          #print(v)
#          if v<1 or v>l:
#              return False
#          j = v-1      # -1 because Index starts from 0
#          flag[j] = 1
#        
#        # Check if any column is missing
#        for c in range(l):
#            if flag[c] != 1:
#                return False
#        flag.clear()
#        
#    # Check the columns
#    for c in range(l):
#        # Initialize flag to zero
#        for r in range(l):
#          flag.append( 0 )
#          #print(flag)
#          #print( c, flag[c] )
#          
#        #  Use flag
#        for r in range(l):
#          v = square[r][c]
#          #print(v)
#          if v<1 or v>l:
#              return False
#          i = v-1      # -1 because Index starts from 0
#          flag[i] = 1
#        
#        # Check if any column is missing
#        for r in range(l):
#            if flag[r] != 1:
#                return False
#        flag.clear()
#        
#    return True
#
#print( check_sudoku(correct) )
#print( check_sudoku(incorrect) ) 
#print( check_sudoku(incorrect2) )
#print( check_sudoku(incorrect3) )
#print( check_sudoku(incorrect4) )
##print( check_sudoku(incorrect5) )

# sudoku.py
#correct = [[1,2,3],
#           [2,3,1],
#           [3,1,2]]
#
#incorrect = [[1,2,3,4],
#             [2,3,1,3],
#             [3,1,2,3],
#             [4,4,4,4]]
#
#incorrect2 = [[1,2,3,4],
#             [2,3,1,4],
#             [4,1,2,3],
#             [3,4,1,2]]
#
#incorrect3 = [[1,2,3,4,5],
#              [2,3,1,5,6],
#              [4,5,2,1,3],
#              [3,4,5,2,1],
#              [5,6,4,3,2]]
#
#incorrect4 = [['a','b','c'],
#              ['b','c','a'],
#              ['c','a','b']]
#
#incorrect5 = [ [1, 1.5],
#               [1.5, 1]]
               
# Define a function check_sudoku() here:
   
    
#print(check_sudoku(incorrect))
#>>> False

#print(check_sudoku(correct))
#>>> True

#print(check_sudoku(incorrect2))
#>>> False

#print(check_sudoku(incorrect3))
#>>> False

#print(check_sudoku(incorrect4))
#>>> False

#print(check_sudoku(incorrect5))
#>>> False