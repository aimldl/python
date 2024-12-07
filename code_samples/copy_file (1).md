##### aimldl > python3 > web_articles > copy_file.md


[Python : How to copy files from one location to another using shutil.copy()](https://thispointer.com/python-how-to-copy-files-from-one-location-to-another-using-shutil-copy/)


```python3
import shutil

shutil.copy(src, dst, *, follow_symlinks=True)
```

#### Copy a file to other directory
```python3
shutil.copy( file, directory )
```
For example,
```python3
file_input = english-0.wav
dir_output = ~/projects/python3/output
shutil.copy( file_input, dir_output)
```
