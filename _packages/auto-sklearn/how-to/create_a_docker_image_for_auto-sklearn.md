* Draft: 2020-05-22 (Fri)

# Create a Docker Image for auto-sklearn

## Step 1. Prepare a Docker base image

```bash
# Download a base image
$ docker login
$ docker pull aimldl/baseimage_python3.7.6_conda_4.8.3_ubuntu18.04.4
# Run the downloade Docker base image
$ docker run -it -p 8080:8080 aimldl/baseimage_python3.7.6_conda_4.8.3_ubuntu18.04.4 bash
2020-05-22 (Fri) 00:51 (20th week)
Welcome to ubuntu18.04, conda 4.8.3, Python 3.7.6
(base) user@1b2e1ff85526:~$ 
```

## Step 2. Update Ubuntu, Anaconda and pip for Python

```bash
# Ubuntu
$ sudo apt update
$ sudo apt -y upgrade

# Anaconda
$ conda update -n base -c defaults -y conda

# pip for Python
$ pip install --upgrade pip
```

## Step 3. Install auto-sklearn INSIDE the Docker container

An Anaconda virtual environment is recommended. It is assumed that Anaconda virtual environment has already been installed. If not, refer to [Install Anaconda on Linux](../../compuing_environments/anaconda/INSTALL.md) to set up a virtual environment. 

To install auto-sklearn, run the following commands. For details, refer to [Install auto-sklearn](../INSTALL.md).

```bash
# Meet the system requirements
(base) $ sudo apt-get install build-essential swig

# Create an Anaconda virtual environment
(base) $ conda update -n base -c defaults -y conda
(base) $ conda create -n auto-sklearn python=3 anaconda

# Enter the created virtual environment
(base) $ conda activate auto-sklearn
(auto-sklearn) user@1b2e1ff85526:~$ 

# Install all dependencies for auto-sklearn
(auto-sklearn) $ curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip install

# Install auto-sklearn
(auto-sklearn) $ pip install auto-sklearn
```

To verify the installation, run a couple of lines of code with the `autosklearn` module.

```bash
(auto-sklearn) $ python -c "import autosklearn; print( autosklearn.__version__ )"
0.7.0
$
```

The installation is successful if there is no error. Notice auto-sklearn's version is 0.7.0.

## Step 4. Create a Docker base image for audo-sklearn

Get out of the Docker container by pressing `Ctrl+p+q`. `read escape sequence` is shown in the terminal.

```bash
(auto-sklearn) user@1b2e1ff85526:~$ read escape sequence
$ 
```

Check the name of the Docker container under `NAMES`.

```bash
$ docker ps
CONTAINER ID        IMAGE                                                    COMMAND  ...
1b2e1ff85526        aimldl/baseimage_python3.7.6_conda_4.8.3_ubuntu18.04.4   "bash"   ... 
...  CREATED         STATUS              PORTS                    NAMES
...  59 minutes ago  Up 57 minutes       0.0.0.0:8080->8080/tcp   quirky_fermat
```

Create a Docker image with the `docker commit` command.

* The container name is `quirky_fermat`.
* The image name is `aimldl/baseimage_autosklearn0.7.0_python3.7.6_conda4.8.3_ubuntu18.04.4`
  * Note the version of autosklearn (0.7.0) is used here.

```bash
$ docker commit quirky_fermat aimldl/baseimage_autosklearn0.7.0_python3.7.6_conda4.8.3_ubuntu18.04.4
```

Double-check if the image is created with the `docker images` command.

```bash
$ docker images
REPOSITORY                                                              TAG     ...
aimldl/baseimage_autosklearn0.7.0_python3.7.6_conda4.8.3_ubuntu18.04.4  latest  ...

...  IMAGE ID            CREATED             SIZE
...  edefd0226db7        8 seconds ago       9.35GB
$
```

Optionally, upload the created image to Docker Hub with the `docker push` command.

```bash
$ docker login
$ docker push aimldl/baseimage_autosklearn0.7.0_python3.7.6_conda4.8.3_ubuntu18.04.4
$
```

 To verify, use your web browser, log into Docker Hub, and see if the image is uploaded properly.
