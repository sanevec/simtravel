# simtravel
Urban traffic simulator based on a hybrid cellular automata and agent-based model.

Using this tool we can model synthetic and symmetric cities where electric vehicles (EV) and non-electric vehicles (ICEV) are placed. This simulator enables the study of the arrangement of EV charging stations testing three different stations layout:

* A large central station
* Four medium-sized stations distributed around the city
* Multiple small stations scattered all over the city.

The binary files with the application ready to execute can be downloaded from: [release 1](https://github.com/amarogs/simtravel/releases/tag/1.0)

The installation has been carried out on Ubuntu 22.04.2 LTS.

### Installation requisites
Python 3 (tested on version 3.8) as well as the package-management tool pip. Since some parts of the code have to be compiled, the necessary libraries must also be installed.

Install Python 3.8 on Ubuntu
By default, Python 3.8 is not included in Ubuntu. To install it, we need to add the deadsnakes repository, which contains multiple Python versions.

Step 1: Update System
First, we'll need to update the system:

```
sudo apt update
sudo apt upgrade
```

Step 2: Add the Deadsnakes Repository
After that, let's add the deadsnakes repository:

```
sudo add-apt-repository ppa:deadsnakes/ppa
```

Confirm the addition of the repository when prompted. Once that's done, update our packages again:

```
sudo apt update
```

Step 3: Install Python 3.8

Finally, we'll install Python 3.8:

```
sudo apt install python3.8
```

Step 4: Verify the Installation
Once the installation is complete, you can confirm that Python 3.8 is properly installed by checking the version:

```
python3.8 --version
```

We need the python development package too:

```
apt-get install python3.8-dev
```

### Installation
First, create a new Python virtual environment 
 

```
sudo pip3 install virtualenv
python3.8 -m virtualenv simtravel-env
source simtravel-env/bin/activate
```
Then, install all needed module by using the [requirements.txt](./requirements.txt) and compile the code as a Python extension module.

```
pip3 install -r requirements.txt
python3 setup.py build_ext --inplace
```

### Execution
Finally, the execution of the simulation can be done in two different ways. By using the desktop application, and therefore visualizing the result, or by using the parallel script which is much faster due to no visualization at all.

The desktop app can be executed using the file [run_app.py](./scripts/run_app.py) which can be found in the scripts folder.


```
python3 -m scripts.run_app
```

The second way to execute the simulations is through the parallel script. 
First, we need to modify the input parameters. A template of the parameter file can be found on [parameters.yaml](./scripts/parameters.yaml). 
Afterwards, we execute the following command:

```
python3 -m scripts.run -np 16 -pf ./parameters.yaml
```

Where `-np` is the total number of processes that we want to use and `-pf` is the argument to indicate where the parameter file is. 
By default `-np` takes value 1 and `-pf` assumes that the parameter file is inside ./scripts/parameters.yaml.
