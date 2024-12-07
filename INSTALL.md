* Rev.1: 2020-05-25 (Mon)
* Draft: 2016-12-02 (Fri)
# Install Python Packages & Python3
## Install Python packages
* Package can be installed from the official repository or alternative repositories.
  * Official repository: PyPI is a repository of software for the Python programming language. 
### From PyPI (Python Package Index), https://pypi.org/
```bash
# To install the latest version of “SomeProject”, 
$ pip install "SomeProject"

# To install a specific version:
$ pip install "SomeProject==1.4"

# To install greater than or equal to one version and less than another:
$ pip install "SomeProject>=1,<2"

# To install a version that’s “compatible” with a certain version: 4
pip install "SomeProject~=1.4.2"
```

* To specify a list of requirements in a requirements file
```bash
$ pip install -r requirements.txt
```

### From an alternate index (not from PyPI)
```bash
$ pip install --index-url http://my.package.repo/simple/ SomeProject
```
### Both from PyPI and an alternate index
```bash
$ pip install --extra-index-url http://my.package.repo/simple SomeProject
```
* For details, refer to [Installing Packages](https://packaging.python.org/tutorials/installing-packages/).

## Install Python3 (on Ubuntu)
You can install Python 3 while Python 2 remains as the default Python.
```bash
$ sudo apt-get install python3
```
