# inet_4031_adduser_script

# User Creation Script

## Description
This script creates users and assigns groups using a Python script and an input file.

## Input Format
username:password:last:first:groups

## How to Run
sudo ./create-users.py < create-users.input

 Lines starting with # are skipped (comments)
'-' means no group
Script reads input from file 
