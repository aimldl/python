* Rev.1: 2020-05-25 (Mon)
* Draft: 2016-11-25 (Fri)
# Install BeautifulSoup4

If you have installed Anaconda, BeautifulSoup4 is included in Anaconda.

```bash
(base) $ pip install beautifulsoup4
Requirement already satisfied: beautifulsoup4 in /home/aimldl/anaconda3/lib/python3.8/site-packages (4.9.3)
Requirement already satisfied: soupsieve>1.2; python_version >= "3.0" in /home/aimldl/anaconda3/lib/python3.8/site-packages (from beautifulsoup4) (2.0.1)
(base) &
```

To verify, 

```bash
(base) $ python
Python 3.8.5 (default, Sep  4 2020, 07:30:14) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from bs4 import BeautifulSoup
>>> exit()
(base) $
```

## Linux

```bash
$ pip install beautifulsoup4
```

For details, refer to [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

## Windows

### Step 1. Install in the command prompt.
```
> python -m pip install beautifulsoup4
```
The full message is below.
```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\thkim>python -m pip install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.5.1-py3-none-any.whl (83kB)
    100% |################################| 92kB 421kB/s
Installing collected packages: beautifulsoup4
Successfully installed beautifulsoup4-4.5.1

C:\Users\thkim>
```
### Step 2. Verify the installation
```
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> 
```

