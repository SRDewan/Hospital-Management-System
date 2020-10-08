# Hospital-Management-System

Data & Applications Course Project

## Overview

We all have gone to a hospital/clinic at some point in our lives. Their significance cannot be overstated. Thus, the following database structure serves to make it easier for both patients as well as doctors/administration to navigate through the hospital environment. 

The resulting system can keep track of doctor appointments and surgeries enabling both patients to ascertain which doctors are free as well as doctors to keep track of their schedule. The system can also be used to check the availability of rooms such as a ward, operation theatre, etc., to keep track of bills, to maintain an inventory of medicines in the pharmacy and many more applications. Overall, it will automate the entire functioning making it faster, easier and more efficient to use. 

## Steps to run the program

1. Type `pip3 install prettytable`
2. Type `mysql -h <hostname> -u <username> --port=<port number> -p < Hospital.sql`
3. Input your MySQL password when prompted
4. Type `python3 main.py` to start the CLI
5. Enter your username, password, hostname and port number to use the CLI

## Some notes on using the CLI

1. When you are prompted for password, it won't be shown on the screen as you type to protect your password from being seen by somebody else.
2. The fields starting with `*` are optional. You can press `ENTER` to skip them.