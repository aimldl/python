* Draft: 2020-05-22 (Fri)

# Install auto-sklearn

For details, refer to [auto-sklearn > Installation](https://automl.github.io/auto-sklearn/master/installation.html).

## Preprequisites

* System requirements for auto-sklearn

  * Linux operating system
  * Python (>=3.5)
  * C++ compiler (with C++11 supports)
  * SWIG (version 3.0 or later)

* Anaconda virtual environment is recommended.

  * According to [auto-sklearn > Installation](https://automl.github.io/auto-sklearn/master/installation.html),

  * > We recommend installing *auto-sklearn* into a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) or an [Anaconda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## Step 1. Meet the system requirements

```bash
$ sudo apt-get install build-essential swig
```

## Step 2. Create an Anaconda virtual environment

It is assumed that Anaconda virtual environment has already been installed. If not, refer to [Install Anaconda on Linux](../../compuing_environments/anaconda/INSTALL.md).

```bash
(base) $ conda update -n base -c defaults -y conda
(base) $ conda create -n auto-sklearn python=3 anaconda
```

Enter `y` when 

```bash
Proceed ([y]/n)?
```

shows up. 

## Step 3. Enter the created virtual environment

When the virtual environment is created, activate it.

```bash
(base) $ conda activate auto-sklearn
(auto-sklearn) user@1b2e1ff85526:~$ 
```

The leading `(auto-sklearn)` indicates the `base` virtual environment has been switched to `auto-sklearn` virtual environment.

## Step 4. Install all dependencies for auto-sklearn

```bash
(auto-sklearn) $ curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip install
```

The curl command fetches a list of requirements in `requirements.txt`. 

https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt

> ```
> setuptools
> pytest
> Cython
> 
> numpy>=1.9.0
> scipy>=0.14.1
> 
> scikit-learn>=0.22.0,<0.23
> 
> lockfile
> joblib
> psutil
> pyyaml
> liac-arff
> pandas<1.0
> 
> ConfigSpace>=0.4.0,<0.5
> pynisher>=0.4.2
> pyrfr>=0.7,<0.9
> smac>=0.12
> ```

If you are curious, you may open the URL in your web browser. 

The `xargs -n 1 -L 1` command feeds each line of the list into the `pip install` command, which is a compact and elegant way to run:

```bash
pip install setuptools
pip install pytest
  ...
pip install smac>=0.12
```

##### Troubleshooting

If an error occurs, repeat Step1 and check if the system requirment is met by running:

```bash
$ sudo apt-get install build-essential swig
```

## Step 5. Install auto-sklearn

```bash
(auto-sklearn) $ pip install auto-sklearn
```

## Step 6. Verify the proper installation

To verify the installation, run a couple of lines of code with the `autosklearn` module.

```bash
(auto-sklearn) $ python -c "import autosklearn; print( autosklearn.__version__ )"
0.7.0
$
```

The installation is successful if there is no error. Notice auto-sklearn's version is 0.7.0.