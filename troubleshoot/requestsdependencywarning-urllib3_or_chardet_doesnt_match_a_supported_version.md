* ;Draft: 2020-09-24 (Thu)

# RequestsDependencyWarning: urllib3 (1.25.5) or chardet (3.0.4) doesn't match a supported version!

## Problem

```bash
/usr/lib/python3/dist-packages/requests/__init__.py:80: RequestsDependencyWarning: urllib3 (1.25.5) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
```

### Example 

A command like below exhibits the `RequestsDependencyWarning` error.

```bash
$ http -v POST localhost:5000/sign-up name=user3 email=user3@email.com password=pw4user3 profile=myprofile3
/usr/lib/python3/dist-packages/requests/__init__.py:80: RequestsDependencyWarning: urllib3 (1.25.5) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
POST /sign-up HTTP/1.1
  ...
```

### Failed Attempts

Google search results suggest to upgrade `requests`; so I did. None of the following commands failed.

```bash
$ pip install --upgrade requests
$ pip3 install --upgrade requests
$ pip3 install --upgrade chardet
```

### TODO:

This is just a warning. So I'll ignore it and just move on.