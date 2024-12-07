# udacity-ds_and_algos-lesson2-python_refresher-control_structure-exercise_1.py
#
# In the following exercise you will finish writing smallest_positive 
# which is a function that finds the smallest positive number in a list.
#
#def smallest_positive(in_list):
#    # TODO: Define a control structure that finds the smallest positive
#    # number in in_list and returns the correct smallest number.
#    
#    return 0
#
## Test cases
#
#print(smallest_positive([4, -6, 7, 2, -4, 10]))
## Correct output: 2
#
#print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
## Correct output: 0.2

def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    max_pos = 1000000
    min_pos = max_pos
    for num in in_list:
        if (num > 0):
            if ( num < min_pos ):
                min_pos = num
    if ( min_pos == max_pos):
        print("Something's wrong")
        return   # return None
    else:
      return min_pos

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2