# Chapter 5: Making Your Program Interactive

myName = input("ENter your name: ")
myAge = input("Your age: ")

print("My name is ", myName, " and I'm ", myAge, " years old.")
message = 'My name is {0}  and I\'m {1} years old.'.format(myName, myAge)
print(message)

# This is wrong.
# print("My name is {0}  and I'm {1} years old.").format(myName, myAge)

print("My name is %s and I'm %s years old." %(myName, myAge))
# This is wrong.
# print("My name is %s and I'm %i years old." %(myName, myAge))
print("My name is %s and I'm %i years old." %(myName, int(myAge)))

print("My name is {} and I'm {} years old.".format(myName, myAge))
print("My name is {0} and I'm {1} years old.".format(myName, myAge))
print("My name is {1} and I'm {0} years old.".format(myName, myAge))

