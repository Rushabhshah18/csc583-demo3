# CSC583-demo3
A command line tool to connect and query to a mysql database.

## Install Dependencies
Core dependencies
```
sudo apt-get -y install build-essential python-dev python-setuptools aptitude
sudo easy_install pip
sudo pip install virtualenv virtualenvwrapper
```
**Note-** Add these lines to ~/.bashrc for virtualenvwrapper and restart terminal
```
# Virtual Environment
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

Create your own Virtual Environment and work on
```
mkvirtualenv 'env'
workon 'env'
```

## OS Level Requirements 
MySQL Database Connector
```
sudo apt install default-libmysqlclient-dev mysql-client*
```

## VirtualEnv Requirement
```
pip install -r requirements.txt
```

## Accessing database and creating table

+ Connect to MySQL server
```
mysql -u 'username' -p -h 'host'
```
+ Create Database
```
CREATE DATABASE 'dbname';
```
+ Switch to the new database
```
USE dbname;
```
+ Create table called user
    + Copy string in query.txt (location: files/query.txt)
    + Paste the query and hit enter.

## Running Code
```
python demo.py
```
**Note -** Please update database details in settings.py before running the code.