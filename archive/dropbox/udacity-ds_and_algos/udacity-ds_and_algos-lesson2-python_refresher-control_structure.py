# udacity-ds_and_algos-lesson2-python_refresher-control_structure.py


# Examples of iteration with for loops
my_list = [0,1,2,3,4,5]

# Print each value in my_list.
for item in my_list:
  print('The value of item is: ' + str(item))
  
# Print each index and value pair
for i, value in enumerate(my_list):
  print('The index value is: ' + str(i) + '. The value is: '+str(value))
  
# Print from 0 to 9 with a while loops
i = 0
while ( i<10 ):
  print(i)
  i +=1

# Print each key and dictionary value.

my_dict = {'a': 'jill', 'b':'tom','c':'tim'}
for key in my_dict:
  print( key + ',' + my_dict[key])

# Expected results  
#the value of item is: 0
#the value of item is: 1
#the value of item is: 2
#the value of item is: 3
#the value of item is: 4
#the value of item is: 5
#the index value is: 0. the value is: 0
#the index value is: 1. the value is: 1
#the index value is: 2. the value is: 2
#the index value is: 3. the value is: 3
#the index value is: 4. the value is: 4
#the index value is: 5. the value is: 5
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9
#a,jill
#b,tom
#c,tim