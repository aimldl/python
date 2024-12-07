* Rev.2: 2020-06-04 (Thu)
* Rev.1: 2020-05-28 (Thu)
* Draft: 2020-05-12 (Thu)

# Install H2O.ai on Ubuntu Linux
## References
To install H2O, refer to:
* [Downloading & Installing H2O](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/downloading.html)
* [H2O Download page](http://h2o-release.s3.amazonaws.com/h2o/latest_stable.html)

If Java is missing on your Ubuntu, refer to:
* [How To Install Java on Ubuntu 18.04 > Install Java on Ubuntu via Oracle JDK](https://www.hostinger.com/tutorials/install-java-ubuntu)
The Docker baseimage for Ubuntu does not include Java by default. Java must be installed manualy if you intend to run H2O on a custom Docker image.

## Download the H2O server and run it from the command line

### `DOWNLOAD AND RUN` tab

Get started with H2O in 3 easy steps

1. Download H2O. This is a zip file that contains everything you need to get started.

2. From your terminal, run:

```bash
cd ~/Downloads
unzip h2o-3.30.0.7.zip
cd h2o-3.30.0.7
java -jar h2o.jar
```

3. Point your browser to http://localhost:54321 

### `INSTALL IN PYTHON` tab
Use H2O directly from Python

1. Prerequisite: Python 2.7.x, 3.5.x, or 3.6.x

2. Install dependencies (prepending with `sudo` if needed):
```bash
pip install requests
pip install tabulate
pip install "colorama>=0.3.8"
pip install future
```

At the command line, copy and paste these commands one line at a time:

# The following command removes the H2O module for Python.
```bash
pip uninstall h2o
```

# Next, use pip to install this version of the H2O Python module.
```bash
pip install http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/7/Python/h2o-3.30.0.7-py2.py3-none-any.whl
```

Conda Installation

Available at https://anaconda.org/h2oai/h2o/

To install this package with conda run:

conda install -c h2oai h2o

### Step 1. Download H2O.

```bash
$ cd ~/Downloads
$ wget http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/3/h2o-3.30.0.3.zip
```

### Step 2. From your terminal, run:

```bah
$ unzip h2o-3.30.0.3.zip
$ cd h2o-3.30.0.3
$ java -jar h2o.jar
```

Step 3. Point your browser to [http://localhost:54321](http://localhost:54321/)

## Install in the Python package for H2O

H2O can be installed in Python or R. 

### Step 1. Install Python dependencies
Run
```bash
$ pip install requests tabulate "colorama>=0.3.8" future
```
or separately.
```bash
$ pip install requests
$ pip install tabulate
$ pip install "colorama>=0.3.8"
$ pip install future
```

### Step 2. Remove any previous version

```bash
$ pip uninstall h2o
```
If no previous version is installed,
```bash
WARNING: Skipping h2o as it is not installed.
```
### Step 3. Install the latest stable version of the H2O Python module
```bash
$ pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
```

### Step 4. Verify the installation
```bash
$ python -c "import h2o; print(h2o.__version__)"
3.30.0.3
$
```
### Step 5. Run a demo to see H2O at work
This step is optional. However I recommend reading through it because it can serve as a tutorial that teaches "how to use H2O Python package". Run the demo for GLM (Generalized Linear Model) in either way:

#### Run a demo on the command line
```bash
$ python -c "import h2o; h2o.init(); h2o.demo('glm')"
```
#### Run a Python script with the Python codes
Save the above lines of Python codes into `run_h2o_demo.py`
```python
# run_h2o_demo.py
import h2o
h2o.init()
h2o.demo("glm")
```
and run the .py script
```bash
$ python run_h2o_demo.py
```

Refer to the full message of the demo at [Validate the Installation of the H2O Python Module (full message)](https://github.com/aimldl/python3/blob/master/packages/h2o/how_to/validate_the_installation_of_the_h2o_python_module-full_message.md).

## Install Java if your Linux does not include it by default.
The recent Ubuntu Linux comes with the OpenJDK (Java Developement Kit) and Oracle JRE (Java Runtime Environment). So you don't have to install Java manually. However if Java happens to be missing on your Linux, the command to start the H2O server fails as follows.
```bash
$ java -jar h2o.jar
bash: java: command not found
```
To fix this problem, install Java manually. Note:
* The Docker baseimage for Ubuntu does not include Java by default.
* Java must be installed manualy if you intend to run H2O on a custom Docker image.
* Other flavors of Linux may not include the preinstalled Java.

For details, refer to [How To Install Java on Ubuntu 18.04 > Install Java on Ubuntu via Oracle JDK](https://www.hostinger.com/tutorials/install-java-ubuntu).

### Docker container
```bash
$ sudo apt-get install -y software-properties-common
$ sudo add-apt-repository ppa:linuxuprising/java


```

Caution: Oracle Java14 is not supported.
Installing `oracle-java14-installer`
```bash
$ sudo apt-get install -y oracle-java14-installer
```
will fail:
```bash
$ java -jar h2o.jar
Only Java 8, 9, 10, 11, 12 and 13 are supported, system version is 14.0.1
$
```

### Dockerfile
```dockerfile
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:linuxuprising/java
RUN apt-get update -y
RUN apt-get install oracle-java14-installer
```
-------------------
Next: [Validate the Installation of the H2O Python Module (full message)](https://github.com/aimldl/python3/blob/master/packages/h2o/how_to/validate_the_installation_of_the_h2o_python_module-full_message.md)
