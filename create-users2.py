#!/usr/bin/python3

# INET4031
# Tyler Xiong
# Date Created -  3/29
# Date Last Modified - 4/27

# Dry-run mode:
# If user selects Y, the script will NOT execute system commands.
# Instead, it prints what commands would have run.

# Normal mode:
# If user selects N, the script actually creates users, sets passwords,
# and assigns groups using system commands.

# os = runs system commands
# re = checks patterns in text
# sys = reads input from file
import os
import re
import sys


def main():
    mode = input("Dry-run? (Y/N): ")

    dry_run = (mode.upper() == "Y")

    for line in sys.stdin:
        # check if line starts with # (skip line)
        match = re.match("^#",line)
        
        if line.strip() == "":
            continue

        # split line into parts using :
        fields = line.strip().split(':')

        # skip line if it starts with # or has wrong number of fields
        if match:
            if dry_run:
                print("Skipping line:", line.strip())
            continue

        if len(fields) != 5:
            if dry_run:
                print("ERROR: Bad line:", line.strip())
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

        if dry_run:
            print("Dry run:", cmd)
        else:
            os.system(cmd)

        #print message for password
        print("==> Setting the password for %s..." % (username))
        #command to set password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        if dry_run:
            print("Dry run:", cmd)
        else:
            os.system(cmd)

        for group in groups:
            # loop through groups"
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                if dry_run:
                    print("Would run:", cmd)
                else:
                    os.system(cmd)
                

if __name__ == '__main__':
    main()
