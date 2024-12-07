# * Draft: 2021-06-09 (Wed)
# Python | os.environ object, GeeksforGeeks, 2019-05-22
#   https://www.geeksforgeeks.org/python-os-environ-object/

# os.environ[...] = ... sets the environment variable only for the duration of the python process (or its child processes).
#   https://stackoverflow.com/questions/30006722/os-environ-not-setting-environment-variables/30006803

import os
import pprint

# Code #2: Accessing a particular environment variable
home = os.environ['HOME']
print('HOME:', home)

user = os.environ['USER']
print('USER:', user)

# Code #4: Adding a new environment variable
os.environ['GREETINGS'] = 'Hello, world!'
print('GREETINGS:', os.environ['GREETINGS'])

# Code #3: Modifying a environment variable
os.environ['GREETINGS'] = 'Hello, Tensorflow!'
print('GREETINGS:', os.environ['GREETINGS'])

# Code #1: Use of os.environ to get access of environment variables
#   Print the list of user's environment variables

env_var = os.environ
# The following line's output is too lengthy.
# Uncomment it after running all the above commands.
#pprint.pprint( dict(env_var), width = 1)

