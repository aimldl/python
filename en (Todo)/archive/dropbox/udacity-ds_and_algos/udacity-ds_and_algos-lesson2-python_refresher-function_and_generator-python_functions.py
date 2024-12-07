# udacity-ds_and_algos-lesson2-python_refresher-function_and_generator-python_functions.py

# Python Functions

def sum(a,b):
    return a+b

def list_sort(my_list):
    my_list.sort()
    return len(my_list), my_list

# Python Generators
def all_even():
    n=0
    while True:
        yield n
        n +=2
        
my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print( next( my_gen ))
    
# Now go and do some other processing
do_something = 4
do_something += 3
print( do_something )

for i in range(5):
    print( next( my_gen) )
