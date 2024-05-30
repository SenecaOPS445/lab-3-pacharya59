#!/usr/bin/env python3

#Author ID: pacharya(100706225)

import subprocess

# Defining a user-defined function to get free disk space.
def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    # Creating a child process object.
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    result = process.communicate()
    output = result[0].decode('utf-8').strip()
    return output

if __name__ == '__main__':
    print(free_space())

