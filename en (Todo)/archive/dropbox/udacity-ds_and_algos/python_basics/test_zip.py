# zip() in Python
# https://www.geeksforgeeks.org/zip-in-python/

# 1. zip() in Python
name = ["Manjeet", "Nikhil","Shambhavi", "Astha"];
roll_no = [4,1,3,2]
marks = [40,50,60,70]

mapped = zip(name,roll_no,marks)
print(mapped)
# <zip object at 0x7f7aaebc28c8>

mapped = set(mapped)
print("The zipped results is: ", end="")
print(mapped)
print("\n")
# The zipped results is: {('Nikhil', 1, 50), ('Astha', 2, 70), ('Manjeet', 4, 40), ('Shambhavi', 3, 60)}

# 2. How to unzip?
name = ["Manjeet","Nikhil","Shambhavi","Astha"]
roll_no = [4,1,3,2]
#marks = [40, 50, 60, 70]
marks = [40, 50, 60, 70,80]  # Note the extra element of 80 won't be zipped!

mapped = zip(name,roll_no, marks)
print(mapped)
#<zip object at 0x7f7aae3aff08>

mapped = list(mapped)
print("The zipped results i: ", end="")
print(mapped)
print("\n")

# The zipped results i: [('Manjeet', 4, 40), ('Nikhil', 1, 50), ('Shambhavi', 3, 60), ('Astha', 2, 70)]

# Note the difference between set and list is:
#   {('Nikhil', 1, 50), ('Astha', 2, 70), ('Manjeet', 4, 40), ('Shambhavi', 3, 60)}
#   [('Manjeet', 4, 40), ('Nikhil', 1, 50), ('Shambhavi', 3, 60), ('Astha', 2, 70)]
#
# The set starts and ends with {( and )} whereas 
# the list starts and ends with [( and )].
#
# The former is presented in alphabetical order whereas
# the latter is in the order presented.

# Unzipping the values
list_of_name, list_of_roll_no, list_of_marks = zip(*mapped)
print("The unzippped results:")
print("list_of_name: ", end="")
print(list_of_name)
print("list_of_roll_no: ", end="")
print(list_of_roll_no)
print("list_of_marks: ", end="")
print(list_of_marks)
print("\n")

#The unzippped results:
#list_of_name: ('Manjeet', 'Nikhil', 'Shambhavi', 'Astha')
#list_of_roll_no: (4, 1, 3, 2)
#list_of_marks: (40, 50, 60, 70)

# 3. Practical Applications
#A small example of scorecard is demonstrated below.

#There are many possible applications that can be said to be exected using zip,
#be it student database or scorecard or any other utility that requires mapping of groups. 

players = ["Sachin","Sehwag","Gambhir","Dravid","Raina"]
scores = [100,15,17,28,43]

print("players\tscores")
for pl, sc in zip(players, scores):
    print(pl,"\t",sc)