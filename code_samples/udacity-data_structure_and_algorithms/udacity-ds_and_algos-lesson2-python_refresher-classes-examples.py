# udacity-ds_and_algos-lesson2-python_refresher-classes-examples.py

class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age
        
    def birthday(self):
        self.person_age += 1
        
    def getName(self):
        return self.person_name

bob = Person('Bob',32)
print(bob.getName())

bob.birthday()
print( bob.person_age )