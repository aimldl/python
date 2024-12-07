* Draft:
# Run Python with a Few Commands

```
$ python --help
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
-c cmd : program passed in as string (terminates option list)
```

## Example: Hello, world

```bash
$ python -c "print('Hello')"
Hello
$
```
Note: Using double quotes "" around Hello causes an error.
```bash
$ python -c "print("Hello")"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'Hello' is not defined
$
```
## Example: Convert a validation script to a command-line command
Let's convert the following three lines of Python script into a single line command.
```
Optionally initialize H2O in Python and run a demo to see H2O at work.

import h2o
h2o.init()
h2o.demo("glm")
```
The above lines are ran to verify the installation of H2O's open-source Python module available at:
[Downloading & Installing H2O](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/downloading.html) > [Install in Python](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/downloading.html#install-in-python)
```bash
$ python -c "import h2o; h2o.init(); h2o.demo('glm')"
  ...
>>> h2o.init()

(press any key)
```
