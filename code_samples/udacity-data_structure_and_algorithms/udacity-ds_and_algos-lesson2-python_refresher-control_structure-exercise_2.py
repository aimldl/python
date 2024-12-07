# udacity-ds_and_algos-lesson2-python_refresher-control_structure-exercise_2.py

# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def when_offered(courses, course):
    # TODO: Fill out the function here.
    listOfSemesters = []
#    print(course)
#    print('================')
    for semester in courses:
        #print( courses[semester] )
        for course_num in courses[semester]:
            #print(course_num)
            if course_num == course:
              listOfSemesters.append(semester)

    # TODO: Return list of semesters here.  
    return listOfSemesters


print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []

######################

## This exercise uses a data structure that stores Udacity course information.
## The data structure format is:
#
##    { <semester>: { <class>: { <property>: <value>, ... },
##                                     ... },
##      ... }
#
#
#courses = {
#    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
#                           'teacher': 'Dave',
#                           'assistant': 'Peter C.'},
#                 'cs373': {'name': 'Programming a Robotic Car',
#                           'teacher': 'Sebastian',
#                           'assistant': 'Andy'}},
#    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
#                           'teacher': 'Dave',
#                           'assistant': 'Sarah'},
#                 'cs212': {'name': 'The Design of Computer Programs',
#                           'teacher': 'Peter N.',
#                           'assistant': 'Andy',
#                           'prereq': 'cs101'},
#                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
#                           'teacher': 'Steve',
#                           'prereq': 'cs101'},
#                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
#                           'teacher': 'Wes',
#                           'assistant': 'Peter C.',
#                           'prereq': 'cs101'},
#                 'cs373': {'name': 'Programming a Robotic Car',
#                           'teacher': 'Sebastian'},
#                 'cs387': {'name': 'Applied Cryptography',
#                           'teacher': 'Dave'}},
#    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
#                           'teacher': 'Dorina'},
#                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
#                           'teacher': 'Jasper'},
#                     }
#    }
#
#
#def when_offered(courses, course):
#    # TODO: Fill out the function here.
#    
#    # TODO: Return list of semesters here.
#    return None
#
#
#
#print(when_offered(courses, 'cs101'))
## Correct result: 
## ['fall2020', 'spring2020']
#
#print(when_offered(courses, 'bio893'))
## Correct result: 
## []