* Draft: 2020-05-12 (Thu)

# Create a Docker Image for H2O.ai

## Step 1. Prepare a Docker base image.

```bash
# Download a base image
$ docker login
$ docker pull aimldl/baseimage_python3.7.6_conda_4.8.2_ubuntu18.04.4
# Run the downloade Docker base image
$ docker run -it -p 8080:8080 aimldl/baseimage_python3.7.6_conda_4.8.2_ubuntu18.04.4 bash
2020-05-21 (Thu) 04:22 (20th week)
Welcome to ubuntu18.04, conda 4.8.2, Python 3.7.6
(base) user@d24d8fc9d727:~$ 
```

## Step 2. Download & install H2O INSIDE the Docker container

The following commands are used to make a Docker image for H2O.ai. For details on H2O installation, refer to [Downloading & Installing H2O](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/downloading.html).

```bash
# Download H2O
(base) user@d24d8fc9d727:~$ wget http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/3/h2o-3.30.0.3.zip
(base) user@d24d8fc9d727:~$ unzip h2o-3.30.0.3.zip
(base) user@d24d8fc9d727:~$ cd h2o-3.30.0.3
(base) user@d24d8fc9d727:~$ java -jar h2o.jar
```

The java command is not installed and results in an error.

```bash
(base) user@d24d8fc9d727:~/h2o-3.30.0.3$ java -jar h2o.jar
bash: java: command not found
```

### Download and install Java

For details, refer to [How To Install Java On Ubuntu 18.04](https://phoenixnap.com/kb/how-to-install-java-ubuntu).

```bash
$ sudo apt update
$ sudo apt install default-jdk
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 default-jdk : Depends: default-jre (= 2:1.11-68ubuntu1~18.04.1)
               Depends: default-jdk-headless (= 2:1.11-68ubuntu1~18.04.1) but it is not going to be installed
               Depends: openjdk-11-jdk
 jdk-14.0.1 : Depends: libasound2
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
$ sudo apt --fix-broken install
$ sudo apt install default-jdk
$
```

### Test the java command

```bash
(base) user@d24d8fc9d727:~/h2o-3.30.0.3$ java -jar h2o.jar &
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by ml.dmlc.xgboost4j.java.NativeLibLoader (file:/home/user/h2o-3.30.0.3/h2o.jar) to field java.lang.ClassLoader.usr_paths
WARNING: Please consider reporting this to the maintainers of ml.dmlc.xgboost4j.java.NativeLibLoader
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
05-21 08:50:03.368 172.17.0.2:54321      3578   main      INFO: ----- H2O started  -----

  ...
  
05-21 08:50:04.729 172.17.0.2:54321      3578   main      INFO: H2O started in 2327ms
05-21 08:50:04.730 172.17.0.2:54321      3578   main      INFO: 
05-21 08:50:04.730 172.17.0.2:54321      3578   main      INFO: Open H2O Flow in your web browser: http://172.17.0.2:54321
05-21 08:50:04.730 172.17.0.2:54321      3578   main      INFO: 

(base) user@d24d8fc9d727:~/h2o-3.30.0.3$ 
```

Note the ending & after the java command. Without it, the Java command runs in the foreground. With it, it runs in the background. 

## Step 3. Install the H2O Python Module

```bash
# Install in Python dependencies
(base) user@d24d8fc9d727:~$ pip install requests tabulate "colorama>=0.3.8" future
# Install H2O python module
(base) user@d24d8fc9d727:~$ pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
# Validate the installation
(base) user@d24d8fc9d727:~$ python -c "import h2o; h2o.init(); h2o.demo('glm')"
  ...
>>> h2o.init()

(press any key)
```

The full message to `run python -c "import h2o; h2o.init(); h2o.demo('glm')"` is at [Validate the Installation of the H2O Python Module (full message)](validate_the_installation_of_the_h2o_python_module-full_message.md). This message can serve as an example showcasing how to use H2O Python package. I recommend to read through it. Several parts are edited for better readability without hurting the content.

An excerpt of [the full message](validate_the_installation_of_the_h2o_python_module-full_message.md) is below.

```bash
$ python -c "import h2o; h2o.init(); h2o.demo('glm')"
Checking whether there is an H2O instance running at http://localhost:54321 ..... not found.
  ...
>>> # Connect to H2O
>>>
>>> h2o.init()
  ...
cumulative_capture_rate		gain		cumulative_gain
-------------------------	--------	-----------------
0.0434783					150			150
0.0652174					150			150
0.0869565					150			150
0.108696					150			150
0.108696					-100		108.333
0.217391					108.333		108.333
0.282609					25			80.5556
0.369565					100			84.7826
0.565217					87.5		85.7143
0.652174					-9.09091	63.0435
0.782609					25			55.1724
0.869565					-9.09091	44.9275
0.891304					-77.2727	28.125
0.934783					-58.3333	16.8478
0.978261					-54.5455	9.2233
1							-79.1667	0

---- End of Demo ----

Closing connection _sid_9233 at exit
H2O session _sid_9233 closed.
Closing connection _sid_bc7a at exit
H2O session _sid_bc7a closed.
$
```

Make sure there's no H2O in the local machine. Equivalently, no H2O outside the working Docker container in case the external H2O interferes with.

```bash
$ pip uninstall h2o
Found existing installation: h2o 3.30.0.3
Uninstalling h2o-3.30.0.3:
  Would remove:
    /home/aimldl/anaconda3/lib/python3.7/site-packages/h2o-3.30.0.3.dist-info/*
    /home/aimldl/anaconda3/lib/python3.7/site-packages/h2o/*
Proceed (y/n)? ㅛ
Your response ('ㅛ') was not one of the expected responses: y, n
Proceed (y/n)? y
  Successfully uninstalled h2o-3.30.0.3
$
```

### Step 4. Make sure the H2O server runs in the background

Be careful with the Java command. Without running it in the background, the H2O server is not running. So the H2O Python module won't work.

```bash
Checking whether there is an H2O instance running at http://localhost:54321 ..... not found.
Attempting to start a local H2O server...
```

To recap, the following command to verify the proper installation of H2O must run. Hit Ctrl+C to exit the command.

```bash
(base) user@d24d8fc9d727:~/h2o-3.30.0.3$ python -c "import h2o; h2o.init(); h2o.demo('glm')"
Checking whether there is an H2O instance running at http://localhost:54321 . connected.
05-21 08:59:14.962 172.17.0.2:54321      3630   #07154-15 INFO: POST /4/sessions, parms: {}
05-21 08:59:14.964 172.17.0.2:54321      3630   #07154-15 INFO: Locking cloud to new members, because water.api.schemas4.SessionIdV4
05-21 08:59:15.004 172.17.0.2:54321      3630   #07154-16 INFO: POST /99/Rapids, parms: {ast=(setTimeZone "UTC"), session_id=_sid_867f}
05-21 08:59:15.122 172.17.0.2:54321      3630   #07154-17 INFO: GET /3/Capabilities/API, parms: {}
--------------------------  --------------------------------------------------------------
H2O_cluster_uptime:         3 mins 14 secs
H2O_cluster_timezone:       Etc/GMT
H2O_data_parsing_timezone:  UTC
H2O_cluster_version:        3.30.0.3
H2O_cluster_version_age:    7 days, 11 hours and 14 minutes
H2O_cluster_name:           user
H2O_cluster_total_nodes:    1
H2O_cluster_free_memory:    1.914 Gb
H2O_cluster_total_cores:    4
H2O_cluster_allowed_cores:  4
H2O_cluster_status:         accepting new members, healthy
H2O_connection_url:         http://localhost:54321
H2O_connection_proxy:       {"http": null, "https": null}
H2O_internal_security:      False
H2O_API_Extensions:         Amazon S3, XGBoost, Algos, AutoML, Core V3, TargetEncoder, Core V4
Python_version:             3.7.6 final
--------------------------  --------------------------------------------------------------

-------------------------------------------------------------------------------
Demo of H2O's Generalized Linear Estimator.

This demo uploads a dataset to h2o, parses it, and shows a description.
Then it divides the dataset into training and test sets, builds a GLM
from the training set, and makes predictions for the test set.
Finally, default performance metrics are displayed.
-------------------------------------------------------------------------------

>>> # Connect to H2O
>>> h2o.init()

(press any key)
---- Demo aborted ----

Closing connection _sid_867f at exit
05-21 09:02:48.712 172.17.0.2:54321      3630   #07154-18 INFO: DELETE /4/sessions/_sid_867f, parms: {}
H2O session _sid_867f closed.
(base) user@d24d8fc9d727:~/h2o-3.30.0.3$ 
```

## Step 5. Exit the Docker container & make a Docker Image

Hit `Ctrl+p+q` to escape from the Docker container without stopping it.

```bash
  ...
(base) user@d24d8fc9d727:~/h2o-3.30.0.3$ read escape sequence
$ 
```

Create a Docker image

```bash
$ docker commit -a "Tae-Hyung T. Kim, Ph.D." compassionate_lamport aimldl/baseimage_h2o_3.30.0.3_default_jdk_python3.7.6_conda_4.8.2_ubuntu18.04.4
sha256:888a9a0990fc8ac487d730da5c6fdf7c0942c2cdca48a88142e7fe51f9b01253
$ docker images
REPOSITORY                                                                       TAG   ...
aimldl/baseimage_h2o_3.30.0.3_default_jdk_python3.7.6_conda_4.8.2_ubuntu18.04.4  latest...

...  IMAGE ID            CREATED              SIZE
...  888a9a0990fc        About a minute ago   8.03GB
$ docker login
  ...
Login Succeeded
$ docker push aimldl/baseimage_h2o_3.30.0.3_default_jdk_python3.7.6_conda_4.8.2_ubuntu18.04.4
$
```



## Appendix. Start and attach to the Docker container

```bash
$ docker ps -a
CONTAINER ID  IMAGE                                                   COMMAND  ...
d24d8fc9d727  aimldl/baseimage_python3.7.6_conda_4.8.2_ubuntu18.04.4  "bash"   ... 
  ... NAMES
  ... compassionate_lamport
$ docker start compassionate_lamport 
compassionate_lamport
$ docker ps
CONTAINER ID  IMAGE                                                   COMMAND  ...
d24d8fc9d727  aimldl/baseimage_python3.7.6_conda_4.8.2_ubuntu18.04.4  "bash"   ... 
  ... CREATED  		STATUS			PORTS					NAMES
  ... 2 hours ago	Up 2 seconds	0.0.0.0:8080->8080/tcp	compassionate_lamport
$ docker attach compassionate_lamport 
(base) user@d24d8fc9d727:~$ 
```