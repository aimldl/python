* Rev.1: 2020-08-11 (Tue)
* Draft: 2020-08-07 (Fri)

# How to Install H2O on Ubuntu 18.04

## Install H2O directly on Ubuntu
* No Conda virtual environment.
* No Docker environment.
* This is the easiest way from the installation and usage perspective.
* In general, Conda environment is recommended, but it can be confusing for a newbie.

### Summary
Install
* Java Runtime Environment (JRE)
* H2O.ai server
* Python
* Relevant Python dependencies for H2O.ai
* H2O Python package

All the actions are summarized below.
```bash
sudo apt-get install -y default-jre
java --version

# Download the installer file
cd ~/Downloads
unzip h2o-3.30.0.7.zip
cd h2o-3.30.0.7
java -jar h2o.jar
# Run the H2O server in a web browser at http://localhost:54321

sudo apt install -y python-dev python3-dev python-pip python3-pip
pip install requests tabulate "colorama>=0.3.8" future
pip install http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/7/Python/h2o-3.30.0.7-py2.py3-none-any.whl

python -c "import h2o; h2o.init(); h2o.demo('glm')"
```
The above actions are explained below.

### Step 1. Install the default JRE
Run

```bash
$ sudo apt-get install default-jre
```

and verify the installation

```bash
$ java --version
```

### Step 2. Install H2O.ai server
Go to http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/7/index.html

The `Download and Run` tab of the page is below.
```
Get started with H2O in 3 easy steps
1. Download H2O. This is a zip file that contains everything you need to get started.
2. From your terminal, run:

cd ~/Downloads
unzip h2o-3.30.0.7.zip
cd h2o-3.30.0.7
java -jar h2o.jar

3. Point your browser to http://localhost:54321 
```

### Step 3. Install Python
```bash
$ sudo apt install -y python3-dev python3-pip
# $ sudo apt install -y python-dev python3-dev python-pip python3-pip
```

### Step 4. Install the relevant Python dependencies for H2O.ai
```bash
$ pip install requests tabulate "colorama>=0.3.8" future
```

### Step 5. Install H2O
```bash
$ pip3 install http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/7/Python/h2o-3.30.0.7-py2.py3-none-any.whl
```
For Python versio 2, the command is:
```bash
$ pip install http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/7/Python/h2o-3.30.0.7-py2.py3-none-any.whl
```

## Verify the H2O installation
```bash
$ python3 -c "import h2o; print(h2o.__version__)"
3.30.0.7
$

## Run the official demo

```bash
$ python3 -c "import h2o; h2o.init(); h2o.demo('glm')"
```
