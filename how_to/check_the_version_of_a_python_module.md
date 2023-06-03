* Draft: 2020-05-22 (Fri)

# Check the Version of a Python Module

## References

* [Check the version of Python package / library](https://note.nkmk.me/en/python-package-version/)
* [How to check version of python modules?](https://stackoverflow.com/questions/20180543/how-to-check-version-of-python-modules)

## Summary

> Get the version in Python script: `__version__` attribute
>
> Check with pip command
>
> - List installed packages: `pip list`
> - List installed packages: `pip freeze`
> - Check details of installed packages: `pip show`
> - Check with `conda` command: `conda list`

## In a Python script,

```python
import pandas as pd

print(pd.__version__)
# 0.22.0
```

## In a terminal,

```bash
$ python -c "import autosklearn; print( autosklearn.__version__ )"
0.7.0
$
```