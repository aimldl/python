* Draft: 2020-05-07 (Thu)

# Importing Custom Module from Subdirectory

Google search: python import custom module from subdirectory

## [Import a file from a subdirectory?](https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory)

### Question

> I have a file called `tester.py`, located on `/project`.
>
> `/project` has a subdirectory called `lib`, with a file called `BoxTime.py`:
>
> ```none
> /project/tester.py
> /project/lib/BoxTime.py
> ```
>
> I want to import `BoxTime` from `tester`. I have tried this:
>
> ```py
> import lib.BoxTime
> ```
>
> Which resulted:
>
> ```none
> Traceback (most recent call last):
>   File "./tester.py", line 3, in <module>
>     import lib.BoxTime
> ImportError: No module named lib.BoxTime
> ```
>
> Any ideas how to import `BoxTime` from the subdirectory?

### Answer

> Take a look at the Packages documentation (Section 6.4) here: http://docs.python.org/tutorial/modules.html
>
> In short, you need to put a blank file named
>
> ```py
> __init__.py
> ```
>
> in the "lib" directory.