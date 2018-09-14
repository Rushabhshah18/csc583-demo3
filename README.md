# CSC583-demo3
A command line tool to connect and query to a mysql database.

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