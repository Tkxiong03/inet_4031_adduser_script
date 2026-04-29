#!/usr/bin/python3

# INET4031
# Tyler Xiong
# Date Created -  3/29
# Date Last Modified - 4/27

# os = runs system commands
# re = checks patterns in text
# sys = reads input from file
import os
import re
import sys

def main():
    for line in sys.stdin:
        # check if line starts with # (skip line)
        match = re.match("^#",line)

        # split line into parts using :
        fields = line.strip().split(':')

        # skip line if it starts with # or has wrong number of fields
        if match or len(fields) != 5:
            continue

        # get username and password from input
        username = fields[0]
        password = fields[1]
        #combine first and last name
        gecos = "%s %s,,," % (fields[3],fields[2])

        # split groups by comma
        groups = fields[4].split(',')

        # print message for creating user
        print("==> Creating account for %s..." % (username))
        # command to create user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        os.system(cmd)

        #print message for password
        print("==> Setting the password for %s..." % (username))
        #command to set password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        os.system(cmd)
        for group in groups:
            # loop through groups"
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)
                

if __name__ == '__main__':
    main()
