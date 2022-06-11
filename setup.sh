#!/bin/bash
#install Python Dependancies
pip install virtualenv

# Create user/pass variables
read -p "Enter your Oreilly username: " OR_USER
read -p "Enter your Oreilly password: " OR_PASS
echo "user = "$OR_USER"
password = "$OR_PASS"
" | tee ./oreilly_vars.py

#creates a virtual environemnt
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt 

#adding chronjob to run weekly
crontab -l | { cat; echo "@weekly `pwd`/venv/bin/python `pwd`/oreilly.py"; } | crontab -
