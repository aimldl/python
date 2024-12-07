* Draft: 2020.05-25 (Mon)
# urllib
* Note: using the `request` package is recommended instead of the `urllib` package.

## Introduction
`urllib` is a package that collects several modules for working with URLs.

| Module             | Description                                      |
|--------------------|--------------------------------------------------|
| urllib.request     | open and read URLs                               |
| urllib.error       | contains the exceptions raised by urllib.request |
| urllib.parse       | parses URLs                                      |
| urllib.robotparser | parses robots.txt files                          |

Source: [21.5. urllib — URL handling modules](https://docs.python.org/3/library/urllib.html)

## Example of a working code
```python
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def open_url(url):
    try:
        htm_file = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print("The server couldn't be found.")
        return None
    print(url,"is opened")
    return htm_file
```

## urllib.error
| Module                            | Error is raised when                                                                                  |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| urllib.error.URLError             |                                                                                                       |
| urllib.error.HTTPError            |                                                                                                       |
| urllib.error.ContentTooShortError | the amount of the downloaded data detected by urlretrieve() function is less than the expected amount |
